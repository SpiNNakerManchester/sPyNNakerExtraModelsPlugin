from data_specification.enums.data_type import DataType
from spinn_utilities.overrides import overrides
from spynnaker.pyNN.models.neural_properties.neural_parameter import \
    NeuronParameter
from spynnaker.pyNN.models.neuron.synapse_types.abstract_synapse_type \
    import AbstractSynapseType
from spynnaker.pyNN.utilities import utility_calls


class SynapseTypeDelta(AbstractSynapseType):
    """ This represents a synapse type with two delta synapses
    """

    def __init__(self, n_neurons, initial_input_exc, initial_input_inh):
        AbstractSynapseType.__init__(self)
        self._initial_input_exc = utility_calls.convert_param_to_numpy(
            initial_input_exc, n_neurons)
        self._initial_input_inh = utility_calls.convert_param_to_numpy(
            initial_input_inh, n_neurons)

    def get_n_synapse_types(self):
        return 2

    def get_synapse_id_by_target(self, target):
        if target == "excitatory":
            return 0
        elif target == "inhibitory":
            return 1
        return None

    def get_synapse_targets(self):
        return "excitatory", "inhibitory"

    def get_n_synapse_type_parameters(self):
        return 0

    def get_synapse_type_parameters(self):
        return []

    def get_n_cpu_cycles_per_neuron(self):
        return 0

    @overrides(AbstractSynapseType.get_synapse_type_initial_buffers_parameters)
    def get_synapse_type_initial_buffers_parameters(self):
        return [
            NeuronParameter(self._initial_input_exc, DataType.S1615),
            NeuronParameter(self._initial_input_inh, DataType.S1615)
        ]
