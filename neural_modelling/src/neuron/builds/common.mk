include ../../../paths.mk
include $(NEURAL_MODELLING_DIRS)/src/paths.mk
STDP := $(TIMING_DEPENDENCE) $(WEIGHT_DEPENDENCE)
include $(NEURAL_MODELLING_DIRS)/src/neuron/builds/classes.mk
include $(NEURAL_MODELLING_DIRS)/src/neuron/builds/neural_build.mk
