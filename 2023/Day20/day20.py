import re
import math

FILE = "d20input"
BUTTON_CLICKS = 1000

R_BROADCAST = 'broadcaster -> (?>[a-z]+, )*(?>[a-z]+)'
R_FLIPFLOP = '%[a-z]+ -> (?>[a-z]+, )*(?>[a-z]+)'
R_CONJUNCTION = '&[a-z]+ -> (?>[a-z]+, )*(?>[a-z]+)'

def parse_to_map(modules):
    return {(matches:=re.findall('[a-z]+', module))[0]: matches[1:] for module in modules}

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        module_list = file.read()

        broadcaster = parse_to_map(re.findall(R_BROADCAST, module_list))
        flip_flops = parse_to_map(re.findall(R_FLIPFLOP, module_list))
        conjunctions = parse_to_map(re.findall(R_CONJUNCTION, module_list))

        typed_modules = dict(flip_flops, **conjunctions)

        active_flops = []
        conjuntion_input_defaults = {con: {k: 0 for k, _ in filter(lambda x: con in x[1], typed_modules.items())} for con in conjunctions}

        sent_signals = [BUTTON_CLICKS, 0]

        for _ in range(BUTTON_CLICKS):
            cur_signals = [('broadcaster', 0, signal) for signal in broadcaster['broadcaster']]

            while cur_signals:
                last_module, pulse, cur_module = cur_signals.pop(0)

                sent_signals[pulse] += 1

                if cur_module not in typed_modules:
                    continue

                next_modules = flip_flops[cur_module] if cur_module in flip_flops else conjunctions[cur_module]

                if cur_module in flip_flops and not pulse:
                    for module in next_modules:
                        cur_signals.append((cur_module, cur_module not in active_flops, module))

                if cur_module in conjunctions:
                    conjuntion_input_defaults[cur_module][last_module] = pulse

                    if pulse and len(conjuntion_input_defaults[cur_module]) == 1:
                        next_pulse = 0
                    elif all(v for v in conjuntion_input_defaults[cur_module].values()):
                        next_pulse = 0
                    else:
                        next_pulse = 1

                    for module in next_modules:
                        cur_signals.append((cur_module, next_pulse, module))

                if last_module in flip_flops:
                    active_flops.append(last_module) if pulse else active_flops.remove(last_module)

        print("Part 1:", math.prod(sent_signals))

    # part two
    with open(FILE) as file:
        module_list = file.read()

        broadcaster = parse_to_map(re.findall(R_BROADCAST, module_list))
        flip_flops = parse_to_map(re.findall(R_FLIPFLOP, module_list))
        conjunctions = parse_to_map(re.findall(R_CONJUNCTION, module_list))

        typed_modules = dict(flip_flops, **conjunctions)

        active_flops = []
        conjuntion_input_defaults = {con: {k: 0 for k, _ in filter(lambda x: con in x[1], typed_modules.items())} for con in conjunctions}

        rx_predecessor = [k for k, _ in filter(lambda x: 'rx' in x[1], typed_modules.items())][0]
        low_rx_state = conjuntion_input_defaults[rx_predecessor].copy()

        low_rx = False
        button_clicks = 0

        while not low_rx:
            if all(v > 0 for v in low_rx_state.values()):
                # Found values for all relevant modules
                break

            button_clicks += 1
            cur_signals = [('broadcaster', 0, signal) for signal in broadcaster['broadcaster']]

            while cur_signals:
                last_module, pulse, cur_module = cur_signals.pop(0)

                if cur_module not in typed_modules:
                    if cur_module == 'rx' and not pulse:
                        # hopefully
                        low_rx == True
                    continue

                next_modules = flip_flops[cur_module] if cur_module in flip_flops else conjunctions[cur_module]

                if last_module in conjuntion_input_defaults[rx_predecessor] and pulse:
                    low_rx_state[last_module] = button_clicks

                if cur_module in flip_flops and not pulse:
                    for module in next_modules:
                        cur_signals.append((cur_module, cur_module not in active_flops, module))

                if cur_module in conjunctions:
                    conjuntion_input_defaults[cur_module][last_module] = pulse

                    if pulse and len(conjuntion_input_defaults[cur_module]) == 1:
                        next_pulse = 0
                    elif all(v for v in conjuntion_input_defaults[cur_module].values()):
                        next_pulse = 0
                    else:
                        next_pulse = 1

                    for module in next_modules:
                        cur_signals.append((cur_module, next_pulse, module))

                if last_module in flip_flops:
                    active_flops.append(last_module) if pulse else active_flops.remove(last_module)

        print("Part 2:", math.lcm(*low_rx_state.values()))