from load_data import load_data

class Bot:
    """
    Bot(self, low, high, from, to) is a class with three vector attributes and
    one scalar attribute. The first is Value, which holds the low and high
    values given to the bot (in that order). The second two are From and To,
    each of which stores the Bot identities that this bot will be receiving the
    low, high values (in that order) From, or giving the low, high values (in
    that order) To, respectively. Lastly, ident stores the identity number of
    the current Bot.
    e.g., if my_bot = Bot(23, [4, 7], [21, 22], [24, 25]),
          then my_bot received 4 from Bot 21 and 7 from Bot 22;
               and gives 4 to Bot 24 and 7 to Bot 25.
    """
    def __init__(self, ident=None, vals=[], From=[],
                 low_to=None, high_to=None):
        self.ident = self._checkIdent(ident)
        self.vals = vals
        self.From = From
        self.low_to = low_to
        self.high_to = high_to
        self.low = None
        self.high = None

    def _checkIdent(self, ident):
        if not (isinstance(ident, float) or isinstance(ident, int)):
            raise Exception('expected ident to be float or int')
        else:
            return ident

    def set_ident(self, ident):
        self.ident = self._checkIdent(ident)
        return

    def get_ident(self):
        return self.ident

    def get_low(self):
        if len(self.vals) > 1:
            return min(self.vals)
        else:
            return None

    def get_high(self):
        if len(self.vals) > 1:
            return max(self.vals)
        else:
            return None

    def add_val(self, val):
        self.vals.append(val)
        return

    def send_val(self, bot_num):
        if bot_num == self.low_to:
            return self.get_low()
        elif bot_num == self.high_to:
            return self.get_high()
        elif bot_num == self.ident:
            return self.vals
        else:
            return

    def _print(self):
        print('Bot number: {}'.format(self.ident))
        print('\tLow: {}'.format(self.get_low()))
        print('\tHigh: {}'.format(self.get_high()))
        print('\tValues: {}'.format(self.vals))
        #print('\tFrom: {}'.format(self.From))
        #print('\tLow to: {}'.format(self.low_to))
        #print('\tHigh to: {}\n'.format(self.high_to))


class BotNet:
    def __init__(self, data):
        self.bots = {}
        for d in data:
            parsed = parse(d)
            if parsed[0] == 'assign':
                print('assigning...')
                print('\t{}'.format(parsed[1:]))
                self.assign(*parsed[1:])
            else:  # parsed[0] == 'trade'
                print('trading...')
                print('\t{}'.format(parsed[1:]))
                self.trade(*parsed[1:])

    def add_bot(self, bot_num):
        if not self.bots.get(bot_num):
            self.bots[bot_num] = Bot(bot_num)

    def trade(self, bot_num, low_to, high_to):
        # create the bots if they don't exist
        self.add_bot(bot_num)
        self.add_bot(low_to)
        self.add_bot(high_to)
        # assign the directed edges
        self.bots[bot_num].low_to = low_to
        self.bots[bot_num].high_to = high_to
        self.bots[low_to].From.append(bot_num)
        self.bots[high_to].From.append(bot_num)
        # assign the values if they exist
        lowval = self.bots[bot_num].get_low()
        highval = self.bots[bot_num].get_high()
        if lowval:
            self.bots[low_to].add_val(lowval)
        if highval:
            self.bots[high_to].add_val(highval)
        return

    def assign(self, bot_num, value):
        self.add_bot(bot_num)
        self.bots[bot_num].add_val(value)
        return

    def _print(self):
        print('Bot Net:')
        for bn in self.bots.keys():
            self.bots[bn]._print()

    def updateFromGraph(self):
        for bot_num in self.bots.keys():
            self.fetchValues(bot_num)

    def fetchValues(self, bot_num, rec_depth=5):
        print('Bot number sought is: {}'.format(bot_num))
        this_bot = self.bots.get(bot_num)
        values = this_bot.vals
        # if the bot has the values,
        if len(values) == 2:
            this_bot.low = min(values)
            this_bot.high = max(values)
        # if the bot does not have the values
        elif rec_depth > 0:
            print('\t{}'.format(this_bot.From))
            from_bots = [self.bots[bn] for bn in this_bot.From]
            for from_bot in from_bots:
                self.fetchValues(from_bot.ident, rec_depth-1)
                values.append(from_bot.send_val(bot_num))
            this_bot.low = min(values)
            this_bot.high = max(values)
        return


def parse(d):
    d = d.split(' ')
    if d[0] == 'value':
        op = 'assign'
        value = int(d[1])
        bot_num = int(d[-1])
        out = (op, bot_num, value)
    elif d[0] == 'bot':
        op = 'trade'
        bot_num = int(d[1])
        low_to = int(d[6])
        high_to = int(d[-1])
        out = (op, bot_num, low_to, high_to)
    else:
        raise Exception('unable to parse; operation not recognized')
    print(out)
    return out


def _main(data):
    botnet = BotNet(data)
    # botnet.updateFromGraph()
    return botnet


def trawl_BNs(d):
    bot_nums = []
    for idd, dd in enumerate(d):
        if dd == 'bot':
            bot_nums.append(int(d[idd+1]))
    return bot_nums


if __name__ == "__main__":
    data = load_data('./input/day10input.txt')
    split_data = [d.split(' ') for d in data]

    max_bot_num = max(max(trawl_BNs(d)) for d in split_data)
    lowmat = np.zeros((max_bot_num+1, max_bot_num+1))
    highmat = np.zeros((max_bot_num+1, max_bot_num+1))

    bots = {}
    for bn in range(max_bot_num+1):
        bots[bn] = {'low': None, 'high': None, 'values': []}

    for d in split_data:
        if d[0] == 'value':
            bots[int(d[-1])]['values'].append(int(d[1]))

    for b in bots.items():
        bvals = b.get('values')
        if len(b.get('values')) == 2:
            b['low'] = min(
