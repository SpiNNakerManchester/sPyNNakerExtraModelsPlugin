from spynnaker.pyNN.utilities import utility_calls
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter
from data_specification.enums.data_type import DataType
from spynnaker.pyNN.models.neuron.threshold_types.abstract_threshold_type \
    import AbstractThresholdType

import numpy


class ThresholdTypeMaassStochastic(AbstractThresholdType):
    """ A stochastic threshold
    """

    @staticmethod
    def default_parameters():
        return {'du_th': 0.5, 'tau_th': 20.0, 'v_thresh': -50.0}

    @staticmethod
    def fixed_parameters():
        return {}

    @staticmethod
    def state_variables():
        params = list()
        return params

    @staticmethod
    def is_array_parameters():
        return {}

    def __init__(self, bag_of_neurons):
        AbstractThresholdType.__init__(self)

        self._n_neurons = len(bag_of_neurons)
        self._atoms = bag_of_neurons

    @property
    def v_thresh(self):
        return self._get_param('v_thresh', self._atoms)

    @v_thresh.setter
    def v_thresh(self, v_thresh):
        self._set_param('v_thresh', v_thresh, self._atoms)

    @property
    def du_th(self):
        return self._get_param('du_th', self._atoms)

    @du_th.setter
    def du_th(self, du_th):
        self._set_param('du_th', du_th, self._atoms)

    @property
    def tau_th(self):
        return self._get_param('tau_th', self._atoms)

    @tau_th.setter
    def tau_th(self, tau_th):
        self._set_param('tau_th', tau_th, self._atoms)

    def _du_th_inv(self, atom_id):
        return numpy.divide(1.0, self._atoms[atom_id].get('du_th'))

    def _tau_th_inv(self, atom_id):
        return numpy.divide(1.0, self._atoms[atom_id].get('tau_th'))

    def get_n_threshold_parameters(self):
        return 3

    def get_threshold_parameters(self, atom_id):
        return [
            NeuronParameter(self._du_th_inv(atom_id), DataType.S1615),
            NeuronParameter(self._tau_th_inv(atom_id), DataType.S1615),
            NeuronParameter(
                self._atoms[atom_id].get('v_thresh'), DataType.S1615)
        ]

    def get_n_cpu_cycles_per_neuron(self):
        return 30
