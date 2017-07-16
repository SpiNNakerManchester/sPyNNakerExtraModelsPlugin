MODELS = IF_cond_exp_stoc \
         IF_curr_exp_stdp_recurrent_pre_stochastic_multiplicative \
         IF_curr_exp_stdp_mad_recurrent_dual_fsm_multiplicative \
         IF_curr_exp_stdp_mad_vogels_2011_additive \
         IF_curr_delta \
         IF_curr_exp_ca2_adaptive \
         IF_curr_exp_stdp_nearest_pair_additive \
         IF_curr_exp_stdp_nearest_pair_multiplicative \
         IF_curr_exp_stdp_pfister_triplet_additive \
         IF_curr_exp_stdp_mad_nearest_pair_additive \
         IF_curr_exp_stdp_mad_nearest_pair_multiplicative \
         IF_curr_exp_stdp_mad_pfister_triplet_additive \
         IF_cond_exp_stdp_mad_nearest_pair_additive \
         IF_curr_comb_exp_2E2I \
         IF_curr_comb_exp_5E5I \
         IF_curr_comb_exp_7E7I \
         IF_curr_comb_exp \
         
BUILD_DIRS := $(addprefix builds/, $(MODELS))

all: $(BUILD_DIRS)
	for d in $(BUILD_DIRS); do (cd $$d; "$(MAKE)") || exit $$?; done

clean: $(BUILD_DIRS)
	for d in $(BUILD_DIRS); do (cd $$d; "$(MAKE)" clean) || exit $$?; done
