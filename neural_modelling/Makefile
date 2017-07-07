MODELS = neuron
BUILD_DIRS := $(addprefix src/, $(MODELS))

all: $(BUILD_DIRS)
	for d in $(BUILD_DIRS); do $(MAKE) -C $$d || exit $$?; done

clean: $(BUILD_DIRS)
	for d in $(BUILD_DIRS); do $(MAKE) -C $$d clean || exit $$?; done
