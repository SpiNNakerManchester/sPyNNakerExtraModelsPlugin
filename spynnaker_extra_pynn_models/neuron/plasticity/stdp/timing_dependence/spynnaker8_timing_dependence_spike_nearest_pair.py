from spynnaker_extra_pynn_models.neuron.plasticity.stdp.\
    commons_between_pynn_versions.timing_dependence_spike_nearest_pair \
    import TimingDependenceSpikeNearestPair as \
    CommonTimingDependenaceSpikeNearestPair


class TimingDependenceSpikeNearestPair(
        CommonTimingDependenaceSpikeNearestPair):

    def __init__(
            self, tau_plus=20.0, tau_minus=20.0, A_plus=0.01, A_minus=0.01):
        CommonTimingDependenaceSpikeNearestPair.__init(
            self, tau_plus=tau_plus, tau_minus=tau_minus)

        self._a_plus = A_plus
        self._a_minus = A_minus

    @property
    def A_plus(self):
        return self._a_plus

    @A_plus.setter
    def A_plus(self, new_value):
        self._a_plus = new_value

    @property
    def A_minus(self):
        return self._a_minus

    @A_minus.setter
    def A_minus(self, new_value):
        self._a_minus = new_value
