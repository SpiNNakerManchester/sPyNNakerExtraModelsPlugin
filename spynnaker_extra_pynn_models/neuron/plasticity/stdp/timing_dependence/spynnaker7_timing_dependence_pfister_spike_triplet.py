from spynnaker.pyNN.models.neuron.plasticity.stdp.timing_dependence.\
    timing_dependence_pfister_spike_triplet import \
    TimingDependencePfisterSpikeTriplet as \
    CommonTimingDependencePfisterSpikeTriplet


class TimingDependencePfisterSpikeTriplet(
        CommonTimingDependencePfisterSpikeTriplet):

    # noinspection PyPep8Naming
    def __init__(self, tau_plus, tau_minus, tau_x, tau_y):
        CommonTimingDependencePfisterSpikeTriplet.__init__(
            self, tau_plus=tau_plus, tau_minus=tau_minus, tau_x=tau_x,
            tau_y=tau_y)
