import sys
import gcc.tree.pprint2
import pprint
from gcc.tree.debug import debug
def append_list(current_list, node):
    if current_list :
        if isinstance(current_list,list):
            current_list.insert(0,node)
        else:
            current_list = [node, current_list]
        result = current_list
    else:
        result = node
    return result

def matches(psr_val, debug=True):
    c =0
    ret = []

    #print("DEBUG START")

    #if psr_val.slice[1].value:
        #print "Token Value:" + psr_val.slice[1].value
        #print "Token Type:" + psr_val.slice[1].type

    #for x in psr_val.slice:
        #print("MATCHES: %s" % x)
    #    pass

#    print("MATCHES: %s" % dir(psr_val.lexer.token) )
#    print("MATCHES: %s" % psr_val.lexer.lexliterals )
#    print("MATCHES: %s" % psr_val.lexer.lexdata )
#    print("MATCHES: %s" % psr_val.lexer.lexmatch.string )
    for group in psr_val.lexer.lexmatch.groups() :
        c = c+1
        if group:
           # print("DEBUG",c,group)
            ret.append(group)
    return ret




def report_stack(psr_val):
#    print (psr_val.parser.symstack)
  # print ( psr_val.parser.symstack[0].reverse())
    #stack = copy.copy(psr_val.parser.symstack)
    for x in psr_val.parser.symstack:
        if x.type == '$end':
            continue
        #print ("Token %s" % x)
  # print (dir(x))
        #print ("Value:%s" % x.value)
        #print ("Type:%s" % x.type)
        if 'lexpos' in dir(x):
            #print ("Lex %s" % x.lexpos)
            #print ("Line %s" % x.lineno)
            pass
        # print (type(x))

def goto_state(p,v):
    #print "going to state %s" % v
    p.lexer.begin(v)  # begin the string group

def goto_initial(p):
    #print 'begin initial'
    #raise Exception('where')
    goto_state(p, 'INITIAL')  # begin the string group



def count_non_null(tok):
    count = 0 
    for v in tok.lexer.lexmatch.groups():
        if v is not None :
            print("check %s %d"  % (v, count))
        count = count + 1


def std_attrs2(psr_val):
    #print "val1: %s " %  psr_val[1]
    #print "val2: %s " %  psr_val[2]
    #print "val3: %s " %  psr_val[3]
#    m=matches(psr_val)
#    print "debug2",m
    type_str= psr_val[1]
    #print "std attrs 2 type_str %s " % psr_val[1]
#    if not type_str :
#        type_str = "UNKNOWN_TODO %s" % m
    #node = tuast.Attr(type_str, psr_val[2])
    #pprint2.pprint(psr_val[0])
    #pprint2.pprint(psr_val[1])
    #pprint2.pprint(psr_val[2])
    #result = append_list(psr_val[3], node)
    return []
def std_attrs(psr_val):
    """
    called for each attribute
    """
    #m=psr_val.slice
#    print "debug1",m
    type_str= psr_val[1]
    assert(type_str)
    #node = tuast.Attr(type_str, psr_val[2])
    #result = append_list(psr_val[3], node)
    return psr_val


# create parser rules
def create_rules(tstr):
    for token in tstr.split():
        token = token.upper()
        func = lambda x: x
        rule = "ntype : %s" % token
        func.__doc__ = rule
        current_module = sys.modules[__name__]
        name = "p_%s" % (token.lower())
        #print "name %s(psr_val):\n    \'%s\'\n    return ntype_base(psr_val)\n" %(name, rule)
        setattr(current_module, name , func)


def emit_parser_rule(base_name, prefix):
    # parser
    rule = "%s_type : %s" % (prefix, base_name)
    parser_name = "p_%s" % (base_name.lower())
    #print "def %s(psr_val):\n    \'%s\'\n    psr_val[0] = %s_base(psr_val)\n" %(parser_name, rule, prefix)

def create_list(a,b):
    return [a,b]
def attr_base(psr_val):
    m = psr_val.slice
    if len(m) > 1:
        attr = m[1].value
    else:
        attr =  ""
    #print "got attr %s" % attr
    return attr

# merge the attributes in the list with the object
def merge_list(t) :
    #pprint.pprint({'mergelist':t})                    
    r =  {}
    if '__type__' in t :
        if t['__type__'] == 'attr_list':
            if 'list' in t:
                if t['list']:
                    r=t['list'] # just use this
                else:
                    #pprint.pprint({'check':t})
                    raise Exception("null")

            if 'attrs' in t:
                #pprint.pprint(t)
                
                if 'type' in t['attrs']:
                    if 'val' in t['attrs']:
                        f = t['attrs']['type']
                        v = t['attrs']['val']
                        #debug ("setting %s = %s in %s" %(f,v, pprint.pformat(r)))
                        r[f]=v
                    #else:

                        #raise Exception(
                        #    pprint.pformat(t['attrs'])
                        #)

            
    #pprint2.pprint({'merged': r})
    return r
