from assignment2 import *


def test_part1():
    assert fairy_tale_length == 792
    assert shout_tale == "ONCE UPON A TIME, IN A KINGDOM FAR, FAR AWAY, THERE LIVED A BEAUTIFUL PRINCESS NAMED ANYA. SHE WAS KIND AND GENTLE, BUT SHE WAS ALSO VERY LONELY. HER PARENTS HAD DIED WHEN SHE WAS YOUNG, AND SHE HAD NO SIBLINGS.  ONE DAY, WHILE WALKING IN THE GARDEN, ANYA SAW A SMALL, GREEN FROG SITTING ON A LILY PAD. SHE FELT SORRY FOR THE FROG AND PICKED IT UP. AS SOON AS SHE TOUCHED IT, THE FROG TURNED INTO A HANDSOME PRINCE! THE PRINCE THANKED ANYA FOR FREEING HIM FROM HIS CURSE AND TOLD HER THAT HE WAS THE PRINCE OF A NEIGHBORING KINGDOM. HE HAD BEEN TURNED INTO A FROG BY A WICKED WITCH AS PUNISHMENT FOR BREAKING HIS PROMISE TO HER. ANYA AND THE PRINCE FELL IN LOVE AND WERE MARRIED. THEY LIVED HAPPILY EVER AFTER, RULING THEIR KINGDOMS TOGETHER AND BRINGING PEACE AND PROSPERITY TO THEIR PEOPLE."
    assert whisper_tale == "once upon a time, in a kingdom far, far away, there lived a beautiful princess named anya. she was kind and gentle, but she was also very lonely. her parents had died when she was young, and she had no siblings.  one day, while walking in the garden, anya saw a small, green frog sitting on a lily pad. she felt sorry for the frog and picked it up. as soon as she touched it, the frog turned into a handsome prince! the prince thanked anya for freeing him from his curse and told her that he was the prince of a neighboring kingdom. he had been turned into a frog by a wicked witch as punishment for breaking his promise to her. anya and the prince fell in love and were married. they lived happily ever after, ruling their kingdoms together and bringing peace and prosperity to their people."
    assert first_char == "O"
    assert middle_char == "S"
    assert last_char == "."



def test_part2():
    assert split_string == ['Once', 'upon', 'a', 'time,', 'in', 'a', 'kingdom', 'far,', 'far', 'away,', 'there', 'lived', 'a', 'beautiful', 'princess', 'named', 'Anya.', 'She', 'was', 'kind', 'and', 'gentle,', 'but', 'she', 'was', 'also', 'very', 'lonely.', 'Her', 'parents', 'had', 'died', 'when', 'she', 'was', 'young,', 'and', 'she', 'had', 'no', 'siblings.', 'One', 'day,', 'while', 'walking', 'in', 'the', 'garden,', 'Anya', 'saw', 'a', 'small,', 'green', 'frog', 'sitting', 'on', 'a', 'lily', 'pad.', 'She', 'felt', 'sorry', 'for', 'the', 'frog', 'and', 'picked', 'it', 'up.', 'As', 'soon', 'as', 'she', 'touched', 'it,', 'the', 'frog', 'turned', 'into', 'a', 'handsome', 'prince!', 'The', 'prince', 'thanked', 'Anya', 'for', 'freeing', 'him', 'from', 'his', 'curse', 'and', 'told', 'her', 'that', 'he', 'was', 'the', 'prince', 'of', 'a', 'neighboring', 'kingdom.', 'He', 'had', 'been', 'turned', 'into', 'a', 'frog', 'by', 'a', 'wicked', 'witch', 'as', 'punishment', 'for', 'breaking', 'his', 'promise', 'to', 'her.', 'Anya', 'and', 'the', 'prince', 'fell', 'in', 'love', 'and', 'were', 'married.', 'They', 'lived', 'happily', 'ever', 'after,', 'ruling', 'their', 'kingdoms', 'together', 'and', 'bringing', 'peace', 'and', 'prosperity', 'to', 'their', 'people.']
    assert queen_tale == "Once upon a time, in a kingdom far, far away, there lived a beautiful queen named Anya. She was kind and gentle, but she was also very lonely. Her parents had died when she was young, and she had no siblings.  One day, while walking in the garden, Anya saw a small, green frog sitting on a lily pad. She felt sorry for the frog and picked it up. As soon as she touched it, the frog turned into a handsome prince! The prince thanked Anya for freeing him from his curse and told her that he was the prince of a neighboring kingdom. He had been turned into a frog by a wicked witch as punishment for breaking his promise to her. Anya and the prince fell in love and were married. They lived happily ever after, ruling their kingdoms together and bringing peace and prosperity to their people."
    assert prince_index == 70
    assert is_traditional == True


def test_part3():
    assert sentence_count == 10
    assert vowel_count == 223

def test_bonus1():
    assert reversed_story == ".elpoep rieht ot ytirepsorp dna ecaep gnignirb dna rehtegot smodgnik rieht gnilur ,retfa reve ylippah devil yehT .deirram erew dna evol ni llef ecnirp eht dna aynA .reh ot esimorp sih gnikaerb rof tnemhsinup sa hctiw dekciw a yb gorf a otni denrut neeb dah eH .modgnik gnirobhgien a fo ecnirp eht saw eh taht reh dlot dna esruc sih morf mih gnieerf rof aynA deknaht ecnirp ehT !ecnirp emosdnah a otni denrut gorf eht ,ti dehcuot ehs sa noos sA .pu ti dekcip dna gorf eht rof yrros tlef ehS .dap ylil a no gnittis gorf neerg ,llams a was aynA ,nedrag eht ni gniklaw elihw ,yad enO  .sgnilbis on dah ehs dna ,gnuoy saw ehs nehw deid dah stnerap reH .ylenol yrev osla saw ehs tub ,eltneg dna dnik saw ehS .aynA deman ssecnirp lufituaeb a devil ereht ,yawa raf ,raf modgnik a ni ,emit a nopu ecnO"

def test_bonus2():
    assert consonant_count == 562