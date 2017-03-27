from spynnaker_extra_pynn_models.neuron.plasticity.stdp.\
    commons_between_pynn_versions.timing_dependence_spike_nearest_pair\
    import TimingDependenceSpikeNearestPair as \
    CommonTimingDependenaceSpikeNearestPair


class TimingDependenceSpikeNearestPair(
        CommonTimingDependenaceSpikeNearestPair):

    def __init__(self, tau_plus=20.0, tau_minus=20.0):
        CommonTimingDependenaceSpikeNearestPair.__init(
            self, tau_plus=tau_plus, tau_minus=tau_minus)
