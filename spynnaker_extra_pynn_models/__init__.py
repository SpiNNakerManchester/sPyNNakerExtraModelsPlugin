from spynnaker_extra_pynn_models import model_binaries

#builds
from spynnaker_extra_pynn_models.neuron.builds.if_curr_delta \
    import IFCurrDelta as IF_curr_delta
from spynnaker_extra_pynn_models.neuron.builds.if_curr_exp_ca2_adaptive \
    import IFCurrExpCa2Adaptive as IF_curr_exp_ca2_adaptive
from spynnaker_extra_pynn_models.neuron.builds.if_cond_exp_stoc \
    import IFCondExpStoc as IF_cond_exp_stoc

# plastic timing spynnaker 7
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .spynnaker7_timing_dependence_recurrent\
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .spynnaker7_timing_dependence_vogels_2011\
    import TimingDependenceVogels2011 as Vogels2011Rule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .spynnaker7_timing_dependence_spike_nearest_pair import \
    TimingDependenceSpikeNearestPair as \
    SpYNNaker7TimingDependenceSpikeNearestPair
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .spynnaker7_timing_dependence_pfister_spike_triplet import \
    TimingDependencePfisterSpikeTriplet as \
    SpYNNaker7TimingDependencePfisterSpikeTriplet

# plastic timing spynnaker 8
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .spynnaker8_timing_dependence_pfister_spike_triplet import \
    TimingDependencePfisterSpikeTriplet as \
    SpYNNaker8TimingDependencePfisterSpikeTriplet
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .spynnaker8_timing_dependence_spike_nearest_pair import \
    TimingDependenceSpikeNearestPair as \
    SpYNNaker8TimingDependenceSpikeNearestPair

# plastic weight spynnaker 7
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.wight_dependence\
    .spynnaker7_weight_dependence_additive_triplet import \
    WeightDependenceAdditiveTriplet as \
    SpYNNaker7WeightDependenceAdditiveTriplet

# plastic weights spynnaker 8
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.wight_dependence\
    .spynnaker8_weight_dependence_additive_triplet import \
    WeightDependenceAdditiveTriplet as \
    SpYNNaker8WeightDependenceAdditiveTriplet

__all__ = ['IF_curr_delta', 'IF_curr_exp_ca2_adaptive', 'IF_cond_exp_stoc',
           'RecurrentRule', 'Vogels2011Rule', 'model_binaries']


def _init_module():
    # import logging
    import os
    from spynnaker.pyNN.spinnaker_common import SpiNNakerCommon

    # Register this path with SpyNNaker
    SpiNNakerCommon.register_binary_search_path(
        os.path.dirname(model_binaries.__file__))


_init_module()
