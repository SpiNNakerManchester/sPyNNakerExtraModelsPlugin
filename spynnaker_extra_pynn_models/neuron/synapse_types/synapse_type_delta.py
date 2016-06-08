from spynnaker.pyNN.models.neuron.synapse_types.abstract_synapse_type \
    import AbstractSynapseType


class SynapseTypeDelta(AbstractSynapseType):
    """ This represents a synapse type with two delta synapses
    """

    @staticmethod
    def default_parameters():
        return {}

    @staticmethod
    def fixed_parameters():
        return {}

    @staticmethod
    def state_variables():
        params = list()
        return params

    @staticmethod
    def is_array_parameters():
        return {}

    def __init__(self, bag_of_neurons):
        AbstractSynapseType.__init__(self)

        self._n_neurons = len(bag_of_neurons)
        self._atoms = bag_of_neurons

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
