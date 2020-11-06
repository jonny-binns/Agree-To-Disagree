import json
import sadface as sf

sf.config.init("SADFace/test.cfg")
sf.initialise()

sf.set_title("test argument")

#simple argument for testing

#sets conclusion and reason for
con1 = "the beatles are the best band of all time"
prem1 = ["their albums rank among the highest of all time"]
arg1 = sf.add_argument(con_text=con1, prem_text=prem1, con_id=None, prem_id=None)

#opposing point
prem2 = ["pink floyd explored more musically"]
arg2 = sf.add_atom(con_text=con1, prem_text=prem2, con_id=None, prem_id=None)

#conflicing point
prem2 = "according to rolling stone pet sounds by the beach boys is better than any beatles album"
arg2 = sf.add_conflict(arg_id=sf.get_atom_id("their albums rank among the highest of all time"), conflict_text=prem2)

print(sf.prettyprint())
dot = sf.export_dot()#trad=False)    # Uncomment to use the brewer colourscheme
with open('out.dot', 'w') as file:
    file.write(dot)