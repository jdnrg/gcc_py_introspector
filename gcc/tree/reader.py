'''
reader module
'''
import sys
import os
from gcc.tree.debug import debug
#home = os.environ['HOME']
#user = os.environ['USER']
#sys.path.append(home + '/rdflib/')
#sys.path.append(home + '/sparqlwrapper/')
#import urllib.request, urllib.error, urllib.parse
#handler=urllib.request.HTTPHandler(debuglevel=1)
#opener = urllib.request.build_opener(handler)
#urllib.request.install_opener(opener)
#>>> resp=urllib2.urlopen('http://w
#pprint2.pprint(sys.path)
import re
#import traceback


##
from gcc.tree.tu import lex
from gcc.tree.tuparser import parser
import gcc.tree.tuast
import gcc.tree.pprint2
import gcc.tree.nodes
import gcc.tree.attributes
import gcc.tree.nodes


OPRE = r'op\s([0-9]+)\s*:\s\@'
ERE = r'\s([0-9]+)\s+:\s\@'
vals = {}
#seen = {} 
deps = {}
#filename = sys.argv[1].replace(home,'projects')
domain = 'introspector.xyz'
nodetypes = {}

replace = {
    0x07 : "&#x2407;", #escape BEL
    0x1a : "&#xfffd;" # EOF
}

def clean(x):
    new = []
    for c in list(x):
        o= ord(c)
        if o in replace:
            r = replace[o]
            new.append(r)
        else:
            new.append(c)
    return "".join(new)

#rdflib.RDFS.label
def mnt(nt):
    if nt not in nodetypes:
        ntu = rdflib.URIRef('http://' + domain + '/gcc/node_types.owl#' + nt  )
        nodetypes[nt] =ntu
    return nodetypes[nt]

structures={}
def structure(name, nt):
    if name not in structures:
        structures[name]={}

    if nt not in structures[name]:
        ntu = rdflib.URIRef('http://' + domain + '/gcc/' + name + '.owl#' + nt  )
        structures[name][nt] =ntu
        
    return structures[name][nt]

attrs = {}
def attr(nt):
    if nt not in attrs:
        ntu = rdflib.URIRef('http://' + domain + '/gcc/field_types.owl#' + nt  )
        attrs[nt] =ntu
    return attrs[nt]

# def add_field(g, ni, fname, oid):
#     u = rdflib.URIRef('http://' + domain + '/' + filename + '#' + ni  )
#     p = attr(fname)
#     o = rdflib.URIRef('http://' + domain + '/' + filename + '#' + oid)                        
#     g.add([u, p, o])                        

def report(x,l):
    #print("Results1 %s -> %s | %s" % (x.node_id, x.keys(),l))
    assert(x)
    #k = x.keys()
    #assert(k)
    #print l
    #print k
    # nt = x.node_type
    # ni = x.node_id                        
    # u = rdflib.URIRef('http://' + domain + '/' + filename + '#' + ni  )
    # # Literal('foo')
    # g.add([u, rdflib.RDF.type, mnt(nt)])
    # ## add in one link per filename for easy deletion
    # fop = attr("source_file")
    # fo = rdflib.URIRef('http://' + domain + '/' + filename )                        
    # g.add([u, fop, fo])    
    #pprint2.pprint([ l ])
    #pprint2.pprint([ x ])
    # now add the vals
    # if (x.vals):
    #     #pprint2.pprint([ "Vals", x.vals ])
    #     if isinstance(x.vals, list):
    #         for v in x.vals:
    #             if isinstance(v, tuast.Attr):
    #                 p = attr(v.name)
    #                 v2 =v.value
    #                 #pprint2.pprint([v.name, v2, v2.__dict__ ])
    #                 if isinstance(v2, tuast.NodeRef):
    #                     o = rdflib.URIRef('http://' + domain + '/' + filename + '#' + v.value.val)                        
    #                     g.add([u, p, o])                        
    #                 elif isinstance(v2, tuast.Signed):
    #                     g.add([u, p, rdflib.Literal(v2.val)])
    #                 elif isinstance(v2, tuast.Float):
    #                     g.add([u, p, rdflib.Literal(v2.val)])
    #                 elif isinstance(v2, tuast.Struct):
    #                     g.add([u, p, structure("structure",v2.val)])
    #                 elif isinstance(v2, tuast.FileBuiltin):
    #                     g.add([u, p, rdflib.Literal("true")])
    #                 elif isinstance(v2, tuast.Qual):
    #                     g.add([u, p, structure("qual",v2.val)])                        
    #                 elif isinstance(v2, tuast.Artificial):
    #                     g.add([u, p, structure("artificial",v2.val)])
    #                 elif isinstance(v2, tuast.FilePos):
    #                     g.add([u, p, rdflib.Literal(v2.value)])
    #                 elif isinstance(v2, tuast.Link):
    #                     g.add([u, p, structure("link",v2.val)])
    #                 else:
    #                     #pprint2.pprint( v2 )
    #                     pass
    #             elif isinstance(v, tuast.SpecAttr3):
    #                 vn = attr(v.value)
    #                 p = attr(v.name)
    #                 g.add([u, p, vn])                    
    #             elif isinstance(v, tuast.String):
    #                 p = attr("string")
    #                 g.add([u, p, rdflib.Literal(
    #                     clean(v.val) #https://github.com/RDFLib/rdflib/issues/614
    #                 )])
    #             else:
    #                 #pprint2.pprint( ["OTHER", v ] )
    #                 pass
    #     else:
    #         if isinstance(x.vals, tuast.Attr):
    #             if isinstance(x.vals.value, tuast.NodeRef):
    #                 # a tree_list item with a "valu" field
    #                 add_field(g, x.node_id, x.vals.name , x.vals.value.val)                    
    #             else:
    #                 #pprint2.pprint( ["not a node ref", x.vals.value ] )
    #                 #raise Exception("TODO")
    #                 pass
    #         else:
    #             pass
    #             #pprint2.pprint( ["no vals", x ] )
    #             #raise Exception("TODO")
    # else:
    #     if isinstance(x, tuast.AddrExprTyped):
    #         #print "NodeId:" +
    #         #print "node type:" +x.node_type
    #         #print "Vals:" + str(x.vals)
    #         #pprint2.pprint( ["op_0", x.op_0 ] )
    #         #pprint2.pprint( ["expr_type", x.expr_type ] )
    #         add_field(g, x.node_id, "OP0", x.op_0)
    #         add_field(g, x.node_id, "type", x.expr_type)                
    #         #g.add([u, p, structure("link",v2.val)])
    #     elif isinstance(x, tuast.Node):
    #         #print "TODO some node" + str(x)
    #         #pprint2.pprint( ["TODO", x.__dict__ ] )
    #         pass
    #     else:
    #         #pprint2.pprint( ["no vals", x ] )
    #         raise Exception("TODO")
    
def lex(l, rundebug, error_file):
    """
    try and lex the input
    this function was removed, it is used to test the lexer.
    """
    try:
        lex.input(l)
        for tok in iter(lex.token, None):
            pval = repr(tok.value)
            ptype = repr(tok.type)
            if ptype not in vals:
                vals[ptype] = {}
            vals[ptype][pval] = 1
            stack.append(ptype)  # ,pval

    except Exception as exp:
        error_file.write(l + "\n")
        print("LEX ERROR1 %s %s" % (ptype, pval))
        print("L",l)
        print("EXP",exp)
        print("Stack",stack)
        # raise exp
    print ("Line %s" % l)
    #memprofile()
    
    if rundebug:
        #
        pass

def parse_l(l, rundebug, error_file, f):
    '''
    preprocessing of the line
    '''

    pval = None
    ptype = None

    # if the line is empty
    if not l:
        raise Exception()
    # or does not start with @ 
    if l[0] != '@':
        raise Exception()

    stack = []

    # array element 0
    x = re.search(ERE, l)
    while x:
        n = x.group(1)
        # print ("Find %s in %s" % (n,l))
        l = re.sub(r'\s%s\s+:\s\@' % n, " E%s :@" % n, l)
        x = re.search(ERE, l)

    # replace op 0
    x = re.search(OPRE, l)
    while x:
        n = x.group(1)
        # print ("Find %s in %s" % (n,l))
        l = re.sub(r'op\s%s\s*:\s\@' % n, " OP%s :@" % n, l)
        x = re.search(OPRE, l)

    # now try and parse the input
    try:
        x = parser.parse(l, debug=rundebug)

        #memprofile(l)

        if not x:
            error_file.write(l + "\n")
            #print "Error on Line:%s" % l
            #print "Stack:%s" % stack
            #print "parser %s" % pprint2.pformat(parser.__dict__)
            #if not debug:
            #    x = parser.parse(l, debug=True)
        else:
            report(x,l)
            if rundebug:
                debug(("Results1 %s" % x))
            else:
                s = str(x)
                # if not s in seen:
                #     seen[s]=1
                #     if debug:
                #         print("Results2 '%s'" % s)

        if rundebug :
            debug("Stack:%s" % stack)
            print("parser %s" % parser)

        return x
    
    #except QueryBadFormed as e:
    #    raise e
    except Exception as exp:
        print("parse error : "+ l + "\n")
        error_file.write(l + "\n")
        #traceback.print_exc()
        print("Exp",exp)
        print("EXP Line:%s" % l)
        f.write(l + "\n")
        print("EXP Stack:%s" % stack)
        raise exp
    
    #print "Stack:%s" % stack
    return None

def main():
    """
    Reader for a tu file
    """
    print ("going to open %s" % sys.argv[1])
    fd = open(sys.argv[1])
    # open the error file in case there are any errors they will be written here.
    error_file = open(sys.argv[1] + ".err", "w")
    if len(sys.argv) > 2:
        rundebug = True
    else:
        rundebug = False

    f = open ('lasterror.txt','a')

    line = ""
    for l in fd.readlines():
        l = l.strip()
        if len(l) <= 0  :
            continue

        if l[0] == '@':
            if line:
                gcc.tree.nodes.statement(parse_l(line, rundebug, error_file, f))

                
            line = l
        else:
            line = line + " " + l
    fd.close()

    if line:
        gcc.tree.nodes.statement(parse_l(line, rundebug, error_file, f))
    f.close()

if __name__ == '__main__':
    main()
    #except Exception as e:
    #    print "Error occurred '%s'" % e

    #debug_file = open("output.debug", "w")
    #debug_file.write("data=%s" % pprint2.pformat(deps))
    #debug_file.close()

    #print "\n".join(sorted(seen.keys()))


    #print ""g.serialize("output.xml")
    #types[node_type]=1

    gcc.tree.attributes.report()
    gcc.tree.nodes.report()
