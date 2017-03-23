from spynnaker.pyNN.models.neuron.population_application_vertex import \
    PopulationApplicationVertex
from spynnaker.pyNN.models.neuron.neuron_models\
    .neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from spynnaker.pyNN.models.neuron.input_types.input_type_current \
    import InputTypeCurrent
from spynnaker.pyNN.models.neuron.threshold_types.threshold_type_static \
    import ThresholdTypeStatic
from spynnaker_extra_pynn_models.neuron.synapse_types.synapse_type_delta \
    import SynapseTypeDelta


class IFCurrDelta(PopulationApplicationVertex):
    """ Leaky integrate and fire neuron with an instantaneous \
        current input
    """
    model_based_max_atoms_per_core = 255

    neuron_model = NeuronModelLeakyIntegrateAndFire
    synapse_type = SynapseTypeDelta
    input_type = InputTypeCurrent
    threshold_type = ThresholdTypeStatic

    binary_name = "IF_curr_delta.aplx"
    model_name = "IF_curr_delta"

    @staticmethod
    def get_max_atoms_per_core():
        return IFCurrDelta._model_based_max_atoms_per_core

    @staticmethod
    def set_max_atoms_per_core(new_value):
        IFCurrDelta._model_based_max_atoms_per_core = new_value
