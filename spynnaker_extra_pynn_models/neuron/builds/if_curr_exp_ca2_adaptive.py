from spynnaker.pyNN.models.neuron.abstract_population_vertex import \
    AbstractPopulationVertex
from spynnaker.pyNN.models.neuron.neuron_models\
    .neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_exponential \
    import SynapseTypeExponential
from spynnaker.pyNN.models.neuron.input_types.input_type_current \
    import InputTypeCurrent
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static \
    import ThresholdTypeStatic
from spynnaker_extra_pynn_models.neuron\
    .additional_inputs.additional_input_ca2_adaptive \
    import AdditionalInputCa2Adaptive


class IFCurrExpCa2Adaptive(AbstractPopulationVertex):
    """ Model from Liu, Y. H., & Wang, X. J. (2001). Spike-frequency\
        adaptation of a generalized leaky integrate-and-fire model neuron. \
        Journal of Computational Neuroscience, 10(1), 25-45. \
        doi:10.1023/A:1008916026143
    """

    _model_based_max_atoms_per_core = 255

    default_parameters = {
        'tau_m': 20.0, 'cm': 1.0, 'v_rest': -65.0, 'v_reset': -65.0,
        'v_thresh': -50.0, 'tau_syn_E': 5.0, 'tau_syn_I': 5.0,
        'tau_refrac': 0.1, 'i_offset': 0,
        'tau_ca2': 50.0, "i_ca2": 0.0, "i_alpha": 0.1}

    def __init__(
            self, n_neurons, machine_time_step, timescale_factor,
            spikes_per_second=None, ring_buffer_sigma=None, constraints=None,
            label=None,
            tau_m=default_parameters['tau_m'], cm=default_parameters['cm'],
            v_rest=default_parameters['v_rest'],
            v_reset=default_parameters['v_reset'],
            v_thresh=default_parameters['v_thresh'],
            tau_syn_E=default_parameters['tau_syn_E'],
            tau_syn_I=default_parameters['tau_syn_I'],
            tau_refrac=default_parameters['tau_refrac'],
            i_offset=default_parameters['i_offset'],
            tau_ca2=default_parameters["tau_ca2"],
            i_ca2=default_parameters["i_ca2"],
            i_alpha=default_parameters["i_alpha"], v_init=None):

        neuron_model = NeuronModelLeakyIntegrateAndFire(
            n_neurons, machine_time_step, v_init, v_rest, tau_m, cm, i_offset,
            v_reset, tau_refrac)
        synapse_type = SynapseTypeExponential(
            n_neurons, machine_time_step, tau_syn_E, tau_syn_I)
        input_type = InputTypeCurrent()
        threshold_type = ThresholdTypeStatic(n_neurons, v_thresh)
        additional_input = AdditionalInputCa2Adaptive(
            n_neurons, machine_time_step, tau_ca2, i_ca2, i_alpha)

        AbstractPopulationVertex.__init__(
            self, n_neurons=n_neurons, binary="IF_curr_exp_ca2_adaptive.aplx",
            label=label,
            max_atoms_per_core=(
                IFCurrExpCa2Adaptive._model_based_max_atoms_per_core),
            machine_time_step=machine_time_step,
            timescale_factor=timescale_factor,
            spikes_per_second=spikes_per_second,
            ring_buffer_sigma=ring_buffer_sigma,
            model_name="IF_curr_exp_ca2_adaptive", neuron_model=neuron_model,
            input_type=input_type, synapse_type=synapse_type,
            threshold_type=threshold_type, additional_input=additional_input,
            constraints=constraints)

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        """

        :param new_value:
        :return:
        """
        IFCurrExpCa2Adaptive._model_based_max_atoms_per_core = new_value
