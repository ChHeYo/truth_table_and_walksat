import re
import random


def tt_entails(kb, alpha):
    '''main truth-table enumeration method'''
    symbols = list(propositional_symbols(kb + alpha)) # break up kb and alpha into symbols
    return tt_check_all(kb, alpha, symbols, {})


def tt_check_all(kb, alpha, symbols, model):
    '''for recursive call that assign truth value to each symbol'''
    if not symbols:
        if pl_true(kb, model):
            print('\nWhen model is: ')
            print(model)
            print('KB is TRUE.\n')
            if pl_true(alpha, model):
                print('It is entailed by current KB')
            else:
                return True
            # return pl_true(alpha, model) # true in the model and true in the query
        else: # when kb is false -> we don't care because it's irrelevant
            # print('KB is false in this model\n')
            return True
    else:
        p = symbols[0]
        rest = symbols[1:]
        return tt_check_all(kb, alpha, rest, recursive_model(model, p, True)) and \
               tt_check_all(kb, alpha, rest, recursive_model(model, p, False))


def propositional_symbols(kb_and_alpha):
    '''breaking up kb and alpha into symbols'''
    split_symbols = re.split(r"\s|-|,|v|w+\d|[()]|;", kb_and_alpha)  # parsing symbols
    only_symbols = {sym for sym in split_symbols if sym.isalnum()}
    return sorted(only_symbols)


def recursive_model(model, sym, value):
    '''assigning true or false to a symbol'''
    copy_model = model.copy()
    copy_model[sym] = value
    return copy_model


def pl_true(kb, model):
    '''testing whether propositional logic is true in the model'''
    rules = kb.strip(';')  # model is dict
    rules = re.split(r", ", rules)  # string
    # find value of each key that matches with rule and replace them
    rule_number = 1
    rule_dictionary = {}
    for rule in rules:
        # looping over each rule
        rule = re.sub('[\^]', 'and', rule)
        rule = re.sub('(<=>)', 'iff', rule)
        rule = re.sub('(=>)', 'then', rule)
        split_symbols = re.split(r"\s+|(\W+)", rule)
        erase_empty = [sym for sym in split_symbols if sym]
        # print(erase_empty)
        new_list = []
        for each in erase_empty:
            # looping over each character in a rule
            if model.get(each) is True:
                new_list.append(str(True))
            elif model.get(each) is False:
                new_list.append(str(False))
            elif model.get(each) is None:
                if each == '-':
                    new_list.append('not')
                elif each == 'v':
                    new_list.append('|')
                elif each == 'and':
                    new_list.append('&')
                elif each == 'then':
                    new_list.append('then')
                elif each == 'iff':
                    new_list.append('==')
                else:
                    new_list.append(each)
        replace_by_true_false = " ".join(new_list)
        # to perform implication elimination
        implication_elimination = []
        if 'then' in replace_by_true_false:
            implication_elim = replace_by_true_false.split('then')
            for negation in implication_elim[:-1]:
                negation = '( not ' + negation + ') '
                implication_elimination.append(negation)
            implication_elimination.append(implication_elim[-1])
            replace_by_true_false = "or".join(implication_elimination)
        else:
            pass
        rule_value = eval(replace_by_true_false)
        rule_dictionary[rule_number] = rule_value
        rule_number += 1
    # print(rule_dictionary)
    do_rules_hold = True
    for key, value in rule_dictionary.items():
        if value is False:
            do_rules_hold = False
    return do_rules_hold

# A sentence is satisfiable if it is true in, or satisfied by, some model
def walk_sat(clauses, p=0.5, max_flips=50):
    '''walk_sat algorithm'''
    # clauses => a set of clauses in propositional logic (clause: a disjunction of literals)
    # p => the probabiliy of choosing to do a 'random walk' move (usually 0.5)
    # max_flips => number of flips allowed before giving up

    # break clauses into individual clauses
    clause = [clause for clause in clauses.split(',')]

    # break up clauses into symbols in order to assign truth values
    symbols = propositional_symbols(clauses)

    # random assignment of true or false to the symbols symbols
    model = {}
    for each in symbols:
        model[each] = random.choice([True, False])
    
    print('\nmodel: ' + str(model) + '\n')
    for flip in range(max_flips):
        satisfied_ones, unsatisfied_ones = [], []

        for each_clause in clause:
            if pl_true(each_clause, model):
                satisfied_ones.append(each_clause)
            else:
                unsatisfied_ones.append(each_clause)
            
        # if unsatisifed_ones is empty, then clauses are satisifed within the model
        if not unsatisfied_ones:
            # return successful model
            print('\n** Model that satisfies given clauses: ')
            return model

        print('unsatisfied: ' + str(unsatisfied_ones) + '\n')
        # randomly select a clause from clauses that are not satisfied
        random_false_clause = random.choice(unsatisfied_ones)

        # with probability p
        # flip the value in model of a randomly selected symbol from clause
        probability = random.random()
        print('probability: ' + str(probability))

        if p > probability:
            symbol_to_be_flipped = random.choice(
                propositional_symbols(random_false_clause))
            print('\nThe value of ' + str(symbol_to_be_flipped) + ' will be flipped.')
        else:
            num_of_satisfied_clauses = {}
            for flipped in propositional_symbols(random_false_clause):
                counter = 0
                # for each symbol in a randomly picked clause that was false
                # flip it and change the value of the symbol that gives
                # the maximum number of satisfied clauses
                model[flipped] = not model[flipped]
                # loop over each clause again with the changed value
                for cl in clause:
                    if pl_true(cl, model):
                        # add to counter
                        counter += 1
                # resetting the value after simulation
                model[flipped] = not model[flipped]
                num_of_satisfied_clauses[flipped] = counter
            symbol_to_be_flipped = max(
                num_of_satisfied_clauses, key=num_of_satisfied_clauses.get)
            print('\nFlipping ' + str(symbol_to_be_flipped) + 
            ' gives us ' + str(num_of_satisfied_clauses[symbol_to_be_flipped]) 
            + ' satisifed clauses')

        # change the value of a symbol in the model
        model[symbol_to_be_flipped] = not model[symbol_to_be_flipped]

    # return failure
    return None


if __name__ == '__main__':
    for i in range(1, 6):
        print('Booting...')
        print('\nProblem ' + str(i))
        knowledge_base = input('Enter knowledge base: ')
        entailment = input('What do we need to prove? ')
        print('\n --- Using tt-entailment ---')
        tt_entails(knowledge_base, entailment)
        print('\n --- Using WalkSAT ---')
        print(walk_sat(knowledge_base))