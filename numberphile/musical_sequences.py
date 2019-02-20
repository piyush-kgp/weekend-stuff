
from mido import Message, MidiFile, MidiTrack


def timer(func):
    import time
    def f(*args, **kwargs):
        before = time.time()
        rv = func(*args, **kwargs)
        after = time.time()
        print('%s ran in %s seconds with args=%s and kwargs=%s' %(func.__name__, after-before, args, kwargs))
        return rv
    return f


def generate_midi_seq(seq,file_name, num_steps = 1000):
    # Tushar's composition
    seq = seq(num_steps)
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    for i in range(num_steps):
        track.append(Message('note_on', note=seq[i]%128, velocity=50, time=seq[i]%128))
        track.append(Message('note_off', note=seq[i]%128, velocity=50, time=seq[i]%128))
    mid.save(file_name)


@timer
def generate_midi_seq(seq, file_name, num_steps = 1000):
    # Pure sequence
    seq = seq(num_steps)
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message('program_change', program=12, time=0))
    for i in range(num_steps):
        track.append(Message('note_on', note=seq[i]%128, velocity=50, time=64))
        track.append(Message('note_off', note=seq[i]%128, velocity=50, time=64))
    mid.save(file_name)


def recamanSequence(num_steps):
    recaman = [0]
    for ctr in range(1, num_steps):
        last_num = recaman[-1]
        if last_num-ctr not in recaman and last_num-ctr>0:
            recaman.append(last_num-ctr)
        else:
            recaman.append(last_num+ctr)
    return recaman


def fibonacci(num_steps):
    seq = [0, 1]
    while len(seq)<num_steps:
        seq.append(seq[-2]+seq[-1])
    return seq


def GeestSequence(num_steps=1000):
    seq=[0]
    for i in range(num_steps):
        lst = seq[-1]
        nxt = lst+1
        lst_dgts = set(str(lst))
        nxt_dgts = set(str(nxt))
        while len(nxt_dgts.intersection(lst_dgts))>0:
            nxt+=1
            nxt_dgts = set(str(nxt))
        seq.append(nxt)
    return seq


if __name__=='__main__':
    generate_midi_seq(file_name='recaman_tushar.mid', seq=recamanSequence)
    generate_midi_seq(file_name='fib.mid', seq=fibonacci)
    generate_midi_seq(file_name='geest.mid', seq=GeestSequence, num_steps=60)
