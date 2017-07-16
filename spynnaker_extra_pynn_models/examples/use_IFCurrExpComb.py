import spynnaker7.pyNN as p
from spynnaker_extra_pynn_models.neuron.builds.if_curr_comb_exp import IFCurrCombExp
import plot_utils
p.setup(0.1)

pop_src1 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src1")
#pop_src2 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src1")
pop_src3 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src1")
#pop_src4 = p.Population(1, p.SpikeSourceArray, {'spike_times': [[1]]}, label="src1")

#IFCurrCombExp.set_excitatory_scalar()

pop_ex = p.Population(1, IFCurrCombExp, {}, label="test")

# define the projection
exc_proj = p.Projection(pop_src1, pop_ex,
        p.OneToOneConnector(weights=1, delays=10), target="excitatory")

inh_proj = p.Projection(pop_src3, pop_ex,
        p.OneToOneConnector(weights=1, delays=20), target="inhibitory")


pop_ex.record()
pop_ex.record_gsyn()
pop_ex.record_v()
p.run(50)

v = pop_ex.get_v()
curr = pop_ex.get_gsyn()
spikes = pop_ex.getSpikes()

plot_utils.plotAll(v, spikes)
plot_utils.plot_gsyn(curr)
p.end()
print "\n job done"