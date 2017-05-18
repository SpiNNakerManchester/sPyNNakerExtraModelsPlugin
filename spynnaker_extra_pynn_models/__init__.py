from spynnaker_extra_pynn_models import model_binaries
# builds spynnaker 7
from spynnaker_extra_pynn_models.neuron.builds.if_cond_exp_stoc \
    import IFCondExpStoc as IF_cond_exp_stoc
from spynnaker_extra_pynn_models.neuron.builds.if_curr_delta \
    import IFCurrDelta as IF_curr_delta
from spynnaker_extra_pynn_models.neuron.builds.if_curr_exp_ca2_adaptive \
    import IFCurrExpCa2Adaptive as IF_curr_exp_ca2_adaptive
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_pfister_spike_triplet import \
    TimingDependencePfisterSpikeTriplet
# plastic timing spynnaker 7
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence.timing_dependence_recurrent \
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence \
    .timing_dependence_spike_nearest_pair import \
    TimingDependenceSpikeNearestPair
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence.timing_dependence_vogels_2011 \
    import TimingDependenceVogels2011 as Vogels2011Rule

# plastic weight spynnaker 7

__all__ = [
    # spynnaker 7 models
    'IF_curr_delta', 'IF_curr_exp_ca2_adaptive', 'IF_cond_exp_stoc',

    # extra
    'model_binaries',

    # spynnaker 7 plastic stuff
    'WeightDependenceAdditiveTriplet',
    'TimingDependencePfisterSpikeTriplet',
    'TimingDependenceSpikeNearestPair',
    'RecurrentRule', 'Vogels2011Rule']


def _init_module():
    # import logging
    import os
    from spynnaker.pyNN.spinnaker_common import SpiNNakerCommon

    # Register this path with SpyNNaker
    SpiNNakerCommon.register_binary_search_path(
        os.path.dirname(model_binaries.__file__))


_init_module()
