import sys
import pygame
import base64
import random
from MidiFile import MIDIFile

from modal_group_markov import ModalGroupMarkov
from tone_system import ToneSystem
import random

def adjust_notes(ts, notes):
    low_limit = -30
    high_limit = 35
    transp_period_notes = 15
    transp_margin = 15

    transp = 0
    last_transp = 0
    new_notes = []

    def transp_up(note, transp, last_transp):
        transp = ts.transpose_octave(transp, 1)
        return note + transp, transp, 0

    def transp_down(note, transp, last_transp):
        transp = ts.transpose_octave(transp, -1)
        return note + transp, transp, 0

    for note in notes:
        new_note = note + transp
        if new_note < low_limit:
            new_note, transp, last_transp = transp_up(note, transp, last_transp)
        elif new_note < (low_limit + transp_margin) and \
                last_transp > transp_period_notes:
            new_note, transp, last_transp = transp_up(note, transp, last_transp)
        elif new_note > high_limit:
            new_note, transp, last_transp = transp_down(note, transp, last_transp)
        elif new_note > (high_limit - transp_margin) and \
                last_transp > transp_period_notes:
            new_note, transp, last_transp = transp_down(note, transp, last_transp)

        #print 'Note: ', note, 'New note: ', new_note
        
        last_transp += 1

        new_notes.append(new_note)

    return new_notes

def save_file(music_file, notes):

    # Create the MIDIFile Object
    MyMIDI = MIDIFile(1)

    #offsets = [4,1,0,0,0,2,0]
    offsets = [0,0,0,2,0,1,3,0]

    # Add track name and tempo. The first argument to addTrackName and
    # addTempo is the time to write the event.
    track = 0
    time = 0
    MyMIDI.addTrackName(track,time,"Sample Track")
    MyMIDI.addTempo(track,time, 90)

    channel = 0
    duration = 0.25
    volume = 80

    time+=1

    new_time = time
    
    for note in notes:
        last_time = new_time
        random.shuffle(offsets)
        offset = offsets[0]

        new_time = time - (duration * offset)
        new_duration = duration * (1 + offset)
        
        if new_time < last_time: 
            new_time = last_time
            new_duration = time + 1 - new_time
        
        pitch = 60 + note
        print new_time, new_duration, pitch
        MyMIDI.addNote(track,channel,pitch,(new_time + 0.05*(random.random()-0.5)),new_duration,volume + int(20*random.random()))
        time += duration
        print 'time is now: ', time
        print 'duration is now: ', duration

    MyMIDI.addNote(track,channel,55,time,2,0)

    binfile = open(music_file, 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()

def play_music(music_file):
    """
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    """
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print "Music file %s loaded!" % music_file
    except pygame.error:
        print "File %s not found! (%s)" % (music_file, pygame.get_error())
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)

music_file = "FishPolka.mid"

freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 1024    # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)

ts = ToneSystem(12)
m = ModalGroupMarkov(ts, [4,5,3,6])

#for i in range(0,10):
#    m.add_notes([0,3,6,7,10])

#for i in range(0,2):
#    m.add_notes([0,2,1,4,5,8])

#for i in range(0,12):
#    m.add_notes([0,1,4,6,7,5])

for i in range(0,30):
    m.add_notes([0,4,7,12,4,7,12,4,7,12])

for i in range(0,10):
    m.add_notes([0,4,7,11,12,4,7,11,12,4])

for i in range(0,10):
    m.add_notes([0,3,7,10,12,3,7,10,12])

for i in range(0,2):
    m.add_notes([0,2,4,8,0,2,4,8,11,15])

seq = m.build_seq(300)

if seq == None:
    print 'no sequence produced'
    sys.exit(1)

notes = adjust_notes(ts, seq.notes)

save_file(music_file, notes)

try:
    # use the midi file you just saved
    play_music(music_file)
except KeyboardInterrupt:
    # if user hits Ctrl/C then exit
    # (works only in console mode)
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.stop()
    raise SystemExit
