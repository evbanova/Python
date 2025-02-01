TONES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
INTERVALS = ('unison', 'minor 2nd', 'major 2nd', 'minor 3rd', 'major 3rd', 'perfect 4th', 'diminished 5th', 'perfect 5th', 'minor 6th', 'major 6th', 'minor 7th', 'major 7th')
SEMITONES = 12

class Tone:
    def __init__(self, tone):
        self.tone = tone

    def __str__(self):
        return str(self.tone)

    def __add__(self, other):
        if isinstance(other, Tone):
            return Chord(self, other)
        elif isinstance(other, Interval):
            semitones = other.semitones % SEMITONES
            self_index = TONES.index(str(self))
            self_index += semitones
            return Tone(TONES[self_index % SEMITONES])
        return NotImplemented

    def __sub__(self, other):
        self_index = TONES.index(str(self))
        if isinstance(other, Tone):
            other_index = TONES.index(str(other))
            return Interval(abs(self_index - other_index))
        elif isinstance(other, Interval):
            semitones = other.semitones % SEMITONES
            self_index -= semitones
            return Tone(TONES[self_index % SEMITONES])
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Tone):
            return self.tone == other.tone
        return False

    #ne znam kakvo tochno oznachava no mi izleze greshka che Tone trqbva da e hashable
    def __hash__(self):
        return hash(self.tone)


class Interval:
    def __init__(self, semitones):
        self.semitones = semitones

    def __str__(self):
        return INTERVALS[self.semitones % SEMITONES] 

    def __add__(self, other):
        if isinstance(other, Tone):
            raise TypeError('Invalid operation')
        elif isinstance(other, Interval):
            return Interval((self.semitones + other.semitones) % SEMITONES)
    
    def __sub__(self, other):
        if isinstance(other, Tone):
            raise TypeError('Invalid operation')
    
    def __neg__(self):
        return Interval(-self.semitones)

  
class Chord:
    def __init__(self, *args):
        tones = list(set(args))
        if len(tones) == 1:
            raise TypeError('Cannot have a chord made of only 1 unique tone')
        else:
            self.root = args[0]            
            self.tones = tones

    def __str__(self):
        output = str(self.root.tone)
        root_index = TONES.index(str(self.root.tone))
        tone_names = {str(tone) for tone in self.tones}
        for tone in TONES[root_index + 1:]:
            if tone in tone_names:
                output += '-' + tone
        for tone in TONES[:root_index]:
            if tone in tone_names:
                output += '-' + tone
        return output
        
    def __add__(self, other):
        if isinstance(other, Tone):
            return Chord(self.root, *self.tones, other)
        elif isinstance(other, Chord):
            return Chord(*self.tones, *other.tones)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Tone):
            if other in self.tones:
                other_index = self.tones.index(other)
                return Chord(*self.tones[:other_index], *self.tones[other_index + 1:])
            else:
               raise TypeError(f'Cannot remove tone {other} from chord {self}') 
        return NotImplemented

    def is_minor(self):
        for tone in self.tones:
            interval = self.root - tone 
            if str(interval) == 'minor 3rd':
                return True
        return False

    def is_major(self):
        for tone in self.tones:
            interval = self.root - tone
            if str(interval) == 'major 3rd':
                return True
        return False

    def is_power_chord(self):
        return not (self.is_minor() or self.is_major())
    
    def transposed(self, interval):
        new_tones = []
        new_tones.append(self.root + interval)
        for tone in self.tones:
            new_tones.append(tone + interval)
        return Chord(*new_tones)