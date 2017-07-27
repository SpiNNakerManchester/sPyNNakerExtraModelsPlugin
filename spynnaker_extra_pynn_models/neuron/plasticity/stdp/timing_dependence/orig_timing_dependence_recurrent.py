import math
import numpy

from data_specification.enums.data_type import DataType

from spynnaker.pyNN.models.neuron.plasticity.stdp.timing_dependence.\
    abstract_timing_dependence import AbstractTimingDependence
from spynnaker_extra_pynn_models.neuron.plasticity.stdp\
    .synapse_structure.synapse_structure_weight_accumulator \
    import SynapseStructureWeightAccumulator
from spynnaker.pyNN.models.neuron.plasticity.stdp.common \
    import plasticity_helpers


class TimingDependenceRecurrent(AbstractTimingDependence):
    def __init__(
            self, accum_decay = 1000.00,
            accum_dep_thresh_excit=-6, accum_pot_thresh_excit=6,
            pre_window_tc_excit=35.0, post_window_tc_excit=35.0, 
            accum_dep_thresh_inhib=-6, accum_pot_thresh_inhib=6,
            pre_window_tc_inhib=35.0, post_window_tc_inhib=35.0, 
            dual_fsm=True, seed=None):
        AbstractTimingDependence.__init__(self)

        self.accum_dep_plus_one_excit  = accum_dep_thresh_excit + 1
        self.accum_pot_minus_one_excit = accum_pot_thresh_excit - 1
        self.pre_window_tc_excit = pre_window_tc_excit
        self.post_window_tc_excit = post_window_tc_excit
        self.accum_dep_plus_one_inhib  = accum_dep_thresh_inhib + 1
        self.accum_pot_minus_one_inhib = accum_pot_thresh_inhib - 1
        self.pre_window_tc_inhib = pre_window_tc_inhib
        self.post_window_tc_inhib = post_window_tc_inhib
        #self.accumulator_depression_plus_one = accumulator_depression + 1
        #self.accumulator_potentiation_minus_one = accumulator_potentiation - 1
        #self.mean_pre_window = mean_pre_window
        #self.mean_post_window = mean_post_window
        self.dual_fsm = dual_fsm
        self.rng = numpy.random.RandomState(seed)

        self._synapse_structure = SynapseStructureWeightAccumulator()

    def is_same_as(self, other):
        if (other is None) or (not isinstance(
                other, TimingDependenceRecurrent)):
            return False
        return ((self.accum_dep_plus_one_excit == other.accum_dep_plus_one_excit) and
                (self.accum_pot_minus_one_excit == other.accum_pot_minus_one_excit) and
                (self.pre_window_tc_excit == other.pre_window_tc_excit) and
                (self.pre_window_tc_excit == other.post_window_tc_excit))
        #return ((self.accumulator_depression_plus_one ==
        #         other.accumulator_depression_plus_one) and
        #        (self.accumulator_potentiation_minus_one ==
        #         other.accumulator_potentiation_minus_one) and
        #        (self.mean_pre_window == other.mean_pre_window) and
        #        (self.mean_post_window == other.mean_post_window))

    @property
    def vertex_executable_suffix(self):
        if self.dual_fsm:
            return "recurrent_dual_fsm"
        return "recurrent_pre_stochastic"

    @property
    def pre_trace_n_bytes(self):

        # When using the separate FSMs, pre-trace contains window length,
        # otherwise it's in the synapse
        return 2 if self.dual_fsm else 0

    def get_parameters_sdram_usage_in_bytes(self):

        # 2 * 32-bit parameters
        # 2 * LUTS with STDP_FIXED_POINT_ONE * 16-bit entries
        return (
            (4 * 2) + (2 * (2 * plasticity_helpers.STDP_FIXED_POINT_ONE)) + 16)

    @property
    def n_weight_terms(self):
        return 1

    def write_parameters(self, spec, machine_time_step, weight_scales):

        # Write parameters
        spec.write_value(data=self.accum_dep_plus_one_excit,  data_type=DataType.INT32)
        spec.write_value(data=self.accum_pot_minus_one_excit, data_type=DataType.INT32)

        # Convert mean times into machine timesteps
        mean_pre_timesteps = (float(self.mean_pre_window) *
                              (1000.0 / float(machine_time_step)))
        mean_post_timesteps = (float(self.mean_post_window) *
                               (1000.0 / float(machine_time_step)))

        # Write lookup tables
        self._write_exp_dist_lut(spec, mean_pre_timesteps)
        self._write_exp_dist_lut(spec, mean_post_timesteps)

        # Write random seeds
        spec.write_value(data=self.rng.randint(0x7FFFFFFF),
                         data_type=DataType.UINT32)
        spec.write_value(data=self.rng.randint(0x7FFFFFFF),
                         data_type=DataType.UINT32)
        spec.write_value(data=self.rng.randint(0x7FFFFFFF),
                         data_type=DataType.UINT32)
        spec.write_value(data=self.rng.randint(0x7FFFFFFF),
                         data_type=DataType.UINT32)

    @property
    def pre_trace_size_bytes(self):
        # When using the separate FSMs, pre-trace contains window length,
        # otherwise it's in the synapse
        return 2 if self.dual_fsm else 0

    @property
    def num_terms(self):
        return 1

    def _write_exp_dist_lut(self, spec, mean):
        for x in range(plasticity_helpers.STDP_FIXED_POINT_ONE):

            # Calculate inverse CDF
            x_float = float(x) / float(plasticity_helpers.STDP_FIXED_POINT_ONE)
            p_float = math.log(1.0 - x_float) * -mean

            p = round(p_float)
            spec.write_value(data=p, data_type=DataType.UINT16)

    @property
    def synaptic_structure(self):
        return self._synapse_structure
