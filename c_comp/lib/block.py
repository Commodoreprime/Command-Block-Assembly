from ..ir import IR

def make_block_name(block_id, props):
    prop_dict = {}
    for prop in props:
        key, value = prop.split('=')
        prop_dict[key.strip()] = value.strip()
    return block_id + ('' if not props else '[%s]' % ','.join(
        '%s=%s' % item for item in prop_dict.items()))

def block_is(visitor, expr):
    assert len(expr.args) >= 2, "block_is takes at least 2 arguments"
    args = []
    for arg in expr.args:
        arg_val = visitor.visit_expression(arg)
        assert isinstance(arg_val, IR.LiteralString), \
               "All arguments to block_is must be constant strings"
        args.append(arg_val)
    loc, block, *props = map(lambda a:a.val, args)
    # TODO possible use of ExecSel
    cmd = 'execute if block %s %s' % (loc, make_block_name(block, props))
    res = IR.Slot(visitor.type('int'))
    visitor.emit(IR.Test(cmd, res))
    return res

def block_set(visitor, expr):
    assert len(expr.args) >= 2, "block_set takes at least 2 arguments"
    args = []
    for arg in expr.args:
        arg_val = visitor.visit_expression(arg)
        assert isinstance(arg_val, IR.LiteralString), \
               "All arguments to block_set must be constant strings"
        args.append(arg_val)
    loc, block, *props = map(lambda a:a.val, args)
    cmd = 'setblock %s %s' % (loc, make_block_name(block, props))
    visitor.emit(IR.Asm((('CMD ' + cmd, None, None),)))

def exports():
    return {
        'block_is': block_is,
        'block_set': block_set,
    }
