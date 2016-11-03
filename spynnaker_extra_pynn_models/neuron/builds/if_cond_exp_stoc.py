from spynnaker.pyNN.models.neuron.population_application_vertex import \
    PopulationApplicationVertex
from spynnaker.pyNN.models.neuron.neuron_models\
    .neuron_model_leaky_integrate_and_fire \
    import NeuronModelLeakyIntegrateAndFire
from spynnaker.pyNN.models.neuron.synapse_types.synapse_type_exponential \
    import SynapseTypeExponential
from spynnaker.pyNN.models.neuron.input_types.input_type_conductance \
    import InputTypeConductance
from spynnaker_extra_pynn_models.neuron.threshold_types\
    .threshold_type_maass_stochastic import ThresholdTypeMaassStochastic


class IFCondExpStoc(PopulationApplicationVertex):

    model_based_max_atoms_per_core = 255

    neuron_model = NeuronModelLeakyIntegrateAndFire
    synapse_type = SynapseTypeExponential
    input_type = InputTypeConductance
    threshold_type = ThresholdTypeMaassStochastic

    binary_name = "IF_cond_exp_stoc.aplx"
    model_name = "IF_cond_exp_stoc"

    @staticmethod
    def set_model_max_atoms_per_core(new_value):
        IFCondExpStoc.model_based_max_atoms_per_core = new_value
