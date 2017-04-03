# Question 2 #
seg = SegByName(".idata")
for head in Heads(SegStart(seg), SegEnd(seg)):
	for x in XrefsTo(head, 0):
		if Name(head) in ["strcpy", "sprintf", "strncpy", "wcsncpy", "swprintf"]:
			print GetFunctionName(x.frm), ":", hex(x.frm), ":", Name(head)
