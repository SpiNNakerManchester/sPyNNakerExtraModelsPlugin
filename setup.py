from setuptools import setup

# short names to get line to fit for pep8
ss = 'spynnaker_extra_pynn_models.neuron.plasticity.stdp.synapse_structure'
std = 'spynnaker_extra_pynn_models.neuron.plasticity.stdp.timing_dependence'

setup(
    name="sPyNNakerExtraModelsPlugin",
    version="3.0.0",
    description="Extra models not in PyNN",
    url="https://github.com/SpiNNakerManchester/sPyNNakerExtraModelsPlugin",
    packages=['spynnaker_extra_pynn_models',
              'spynnaker_extra_pynn_models',
              'spynnaker_extra_pynn_models.model_binaries',
              'spynnaker_extra_pynn_models.neuron',
              'spynnaker_extra_pynn_models.neuron.additional_inputs',
              'spynnaker_extra_pynn_models.neuron.builds',
              'spynnaker_extra_pynn_models.neuron.neural_models',
              'spynnaker_extra_pynn_models.neuron.plasticity',
              'spynnaker_extra_pynn_models.neuron.synapse_types',
              'spynnaker_extra_pynn_models.neuron.threshold_types',
              'spynnaker_extra_pynn_models.neuron.plasticity.stdp',
              ss,
              std],
    package_data={'spynnaker_extra_pynn_models.model_binaries': ['*.aplx']},
    install_requires=['SpyNNaker >= 3.0.0, < 4.0.0']
)
