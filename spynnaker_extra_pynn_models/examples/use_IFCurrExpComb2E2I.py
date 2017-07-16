import spynnaker7.pyNN as p
from spynnaker_extra_pynn_models.neuron.builds.if_curr_comb_exp_2E2I import IFCurrCombExp2E2I
import plot_utils
p.setup(.1)

pop_src = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1, 4]]}, label="src")

#pop_ex = p.Population(1, IFCurrCombExp2E2I, {}, label="test")
pop_ex = p.Population(1, p.IF_curr_exp, {}, label="test")

# define the projection
exc_proj = p.Projection(pop_src, pop_ex,
        p.OneToOneConnector(weights=1, delays=1), target="excitatory")

#exc2_proj = p.Projection(pop_src, pop_ex,
#        p.OneToOneConnector(weights=1, delays=30), target="excitatory2")

#inh_proj = p.Projection(pop_src, pop_ex,
#        p.OneToOneConnector(weights=1, delays=20), target="inhibitory")

#inh2_proj2 = p.Projection(pop_src, pop_ex,
#        p.OneToOneConnector(weights=1, delays=40), target="inhibitory2")


pop_ex.record()
pop_ex.record_gsyn()
pop_ex.record_v()
p.run(100)

v = pop_ex.get_v()
curr = pop_ex.get_gsyn()
spikes = pop_ex.getSpikes()

plot_utils.plotAll(v, spikes)
plot_utils.plot_gsyn(curr)
p.end()
print "\n job done"