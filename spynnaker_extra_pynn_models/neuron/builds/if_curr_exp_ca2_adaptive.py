from spynnaker.pyNN.models.neuron.bag_of_neurons_vertex import \
    BagOfNeuronsVertex
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


class IFCurrExpCa2Adaptive(BagOfNeuronsVertex):
    """ Model from Liu, Y. H., & Wang, X. J. (2001). Spike-frequency\
        adaptation of a generalized leaky integrate-and-fire model neuron. \
        Journal of Computational Neuroscience, 10(1), 25-45. \
        doi:10.1023/A:1008916026143
    """

    model_based_max_atoms_per_core = 255

    neuron_model = NeuronModelLeakyIntegrateAndFire
    synapse_type = SynapseTypeExponential
    input_type = InputTypeCurrent
    threshold_type = ThresholdTypeStatic
    additional_input = AdditionalInputCa2Adaptive

    binary_name = "IF_curr_exp_ca2_adaptive.aplx"
    model_name = "IF_curr_exp_ca2_adaptive"

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        IFCurrExpCa2Adaptive.model_based_max_atoms_per_core = new_value
