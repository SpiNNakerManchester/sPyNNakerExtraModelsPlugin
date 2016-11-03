from pacman.executor.injection_decorator import inject_items
from spynnaker.pyNN.models.neural_properties.neural_parameter \
    import NeuronParameter
from data_specification.enums.data_type import DataType
from spynnaker.pyNN.models.neuron.additional_inputs.abstract_additional_input \
    import AbstractAdditionalInput

import numpy


class AdditionalInputCa2Adaptive(AbstractAdditionalInput):

    @staticmethod
    def default_parameters():
        return {'tau_ca2': 50.0, 'i_ca2': 0.0, 'i_alpha': 0.1}

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

    def __init__(self, neuron_cells):
        AbstractAdditionalInput.__init__(self)

        self._n_neurons = len(neuron_cells)
        self._neuron_cells = neuron_cells

    @property
    def tau_ca2(self):
        return self._get_param('tau_ca2', self._neuron_cells)

    @tau_ca2.setter
    def tau_ca2(self, tau_ca2):
        self._set_param('tau_ca2', tau_ca2, self._neuron_cells)

    @property
    def i_ca2(self):
        return self._get_param('i_ca2', self._neuron_cells)

    @i_ca2.setter
    def i_ca2(self, i_ca2):
        self._set_param('i_ca2', i_ca2, self._neuron_cells)

    @property
    def i_alpha(self):
        return self._get_param('i_alpha', self._neuron_cells)

    @i_alpha.setter
    def i_alpha(self, i_alpha):
        self._set_param('i_alpha', i_alpha, self._neuron_cells)

    def _exp_tau_ca2(self, atom_id, machine_time_step):
        return numpy.exp(
            float(-machine_time_step) /
            (1000.0 * self._neuron_cells[atom_id].get('tau_ca2')))

    def get_n_parameters(self):
        return 3

    @inject_items({"machine_time_step": "MachineTimeStep"})
    def get_parameters(self, atom_id, machine_time_step):
        return [
            NeuronParameter(
                self._exp_tau_ca2(atom_id, machine_time_step), DataType.S1615),
            NeuronParameter(
                self._neuron_cells[atom_id].get('i_ca2'), DataType.S1615),
            NeuronParameter(
                self._neuron_cells[atom_id].get('i_alpha'), DataType.S1615)
        ]

    def get_n_cpu_cycles_per_neuron(self):
        return 3

    def get_dtcm_usage_per_neuron_in_bytes(self):
        return 12

    def get_sdram_usage_per_neuron_in_bytes(self):
        return 12
