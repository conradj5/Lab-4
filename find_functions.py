# Question 3 #
exports = []
# loop through exported funcitons
for i in xrange(GetEntryPointQty()):
	ord = GetEntryOrdinal(i)
	if ord != 0:
		addr = GetEntryPoint(ord)
		exports.append(GetFunctionName(addr))

# recursivly search for xrefs to passed address and print when exported function referenced
def search(addr, imp):
	if GetFunctionName(addr) in exports:
		print GetFunctionName(addr), ":", imp
		return
	else:
		gen_xrefs = XrefsTo(addr, 0)
		for xref in gen_xrefs:
			if GetFunctionName(xref.frm) is not GetFunctionName(addr):
				search(xref.frm, imp)


# find imported functions
seg = SegByName(".idata")
for head in Heads(SegStart(seg), SegEnd(seg)):
	for x in XrefsTo(head, 0):
		if Name(head) in ["strcpy", "sprintf", "strncpy", "wcsncpy", "swprintf", "printf"]:
			search(x.frm, Name(head))
			break # if you only want to print output once for each imported funciton use found
