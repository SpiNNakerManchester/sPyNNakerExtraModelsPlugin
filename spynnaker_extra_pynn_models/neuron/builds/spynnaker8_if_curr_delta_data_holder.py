from spynnaker.pyNN.models.neuron.abstract_population_vertex import \
    AbstractPopulationVertex
from spynnaker8.utilities.data_holder import DataHolder
from spynnaker_extra_pynn_models.neuron.builds.\
    if_curr_delta import IFCurrDelta


class IfCurrDeltaDataHolder(DataHolder):

    def __init__(
            self, spikes_per_second=
            AbstractPopulationVertex.none_pynn_default_parameters[
                'spikes_per_second'],
            ring_buffer_sigma=
            AbstractPopulationVertex.none_pynn_default_parameters[
                'ring_buffer_sigma'],
            incoming_spike_buffer_size=
            AbstractPopulationVertex.none_pynn_default_parameters[
                'incoming_spike_buffer_size'],
            constraints=AbstractPopulationVertex.none_pynn_default_parameters[
                'constraints'],
            label=AbstractPopulationVertex.none_pynn_default_parameters[
                'label'],
            tau_m=IFCurrDelta.default_parameters['tau_m'],
            cm=IFCurrDelta.default_parameters['cm'],
            v_rest=IFCurrDelta.default_parameters['v_rest'],
            v_reset=IFCurrDelta.default_parameters['v_reset'],
            v_thresh=IFCurrDelta.default_parameters['v_thresh'],
            tau_refrac=IFCurrDelta.default_parameters['tau_refrac'],
            i_offset=IFCurrDelta.default_parameters['i_offset'],
            v_init=IFCurrDelta.none_pynn_default_parameters['v_init']):
        DataHolder.__init__(
            self,
            {
                'spikes_per_second': spikes_per_second,
                'ring_buffer_sigma': ring_buffer_sigma,
                'incoming_spike_buffer_size': incoming_spike_buffer_size,
                'constraints': constraints, 'label': label,
                'tau_m': tau_m, 'cm': cm, 'v_rest': v_rest,
                'v_reset': v_reset, 'v_thresh': v_thresh,
                'tau_refrac': tau_refrac, 'i_offset': i_offset,
                'v_init': v_init})

    @staticmethod
    def build_model():
        return IFCurrDelta
