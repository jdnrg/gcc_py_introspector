import pprint
#import traceback

def dfilter(x):
    pass
    

def stk():
    return
    #return traceback.format_stack()[-3:-2]
    
    
def debug(*args,**kvargs):
    return
    dfilter(
        {
            'debug': 'one',
            'args':args,
            'kvargs':kvargs,
            'stack':stk(),
        })
    pass

def debug2(*args,**kvargs):
    return
    dfilter(
        {
            'debug': 'two',
            'args':args,
            'kvargs':kvargs,
            'stack':stk(),
        }
        
    )
    pass

def debug4(*args,**kvargs):
    return
    dfilter(
        {
            'debug': 'four',
            'args':args,
            'kvargs':kvargs,
            'stack':stk(),
        }
        )
    pass

def pprintpprint(x):
    return
    dfilter(        {
        'debug': 'pprintpprint',
        'args':x,
        'stack':stk(),
        })
    pass

def debug3(x):
    return
    dfilter({
        'debug': 'debug3',
        'args':x,
        'stack':stk(),
        })
    pass

def debug_ast(psr_val):
    return
    print(("final attrs %s" % dir(psr_val)))
    print(("doc %s" % psr_val.__doc__))
    # psr_val.__getitem__
    # psr_val.__getslice__
    # psr_val.__init__
    plen = psr_val.__len__()
    print(("len:%s" % plen))
    # '__module__', '__setitem__', 'error',
    print((dir(psr_val.lexer)))
    print(("pos:%s" % psr_val.lexpos))
    # p4: 'action', 'errok', 'errorfunc', 'goto', 'parse', 'parsedebug', 'parseopt', 'parseopt_notrack', 'productions', 'restart', 'statestack', 'symstack']
#    print "p4:%s" % dir(psr_val.parser)
#    print "p4action:%s" % psr_val.parser.action
#    print "p4symstac:%s" % psr_val.parser.symstack
#    print "p4statestack:%s" % psr_val.parser.statestack
#    print "SLICE:%s" % psr_val.slice
#    print "p6:%s" % psr_val.stack
#    print "p2:%s" % psr_val.lineno(plen - 1)
    x = psr_val.lexspan(plen - 1)
#    print (x)
#    print "p1:%s,%s" % x
#    print "p3:%s,%s" % psr_val.linespan(plen - 1)
