import spynnaker_extra_pynn_models.model_binaries as model_binaries

from spynnaker_extra_pynn_models.neuron.builds.if_curr_delta \
    import IFCurrDelta as IF_curr_delta
from spynnaker_extra_pynn_models.neuron.builds.if_curr_exp_ca2_adaptive \
    import IFCurrExpCa2Adaptive as IF_curr_exp_ca2_adaptive
from spynnaker_extra_pynn_models.neuron.builds.if_cond_exp_stoc \
    import IFCondExpStoc as IF_cond_exp_stoc
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .timing_dependence_recurrent\
    import TimingDependenceRecurrent as RecurrentRule
from spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence\
    .timing_dependence_vogels_2011\
    import TimingDependenceVogels2011 as Vogels2011Rule

__all__ = ['IF_curr_delta', 'IF_curr_exp_ca2_adaptive', 'IF_cond_exp_stoc',
           'RecurrentRule', 'Vogels2011Rule', 'model_binaries']


def _init_module():
    # import logging
    import os
    import spynnaker.pyNN

    # Register this path with SpyNNaker
    spynnaker.pyNN.register_binary_search_path(os.path.dirname(
        model_binaries.__file__))


_init_module()
