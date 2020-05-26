# Author: Femke Spaans
# Date: 18-05-2020
# Name: Afvink 4
# Version: 1

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Blast import NCBIWWW
import re


def main():
    seq = "GATGCCCTTTUUUGGUGTCGTACTGC"
    number = check(seq)
    if number == 0:
        dna(seq)
    elif number == 1:
        rna(seq)
    elif number == 2:
        protein(seq)
    else:
        print("This is not DNA, RNA or a protein")


def check(seq):
    """

    :param seq: str
    :return:
    """
    for i in seq:
        check_dna = re.search("[^ATGC*$]", i)
        check_rna = re.search("[^AUGC*$]", i)
        check_protein = re.search("[^GPAVLIMCFYWHKRQNEDST*$]", i)
        if check_dna == None:
            print("This is DNA")
            return 0
        elif check_rna == None:
            print("This is RNA")
            return 1
        elif check_protein == None:
            print("This is a protein")
            return 2
        else:
            return 3


    # messenger_rna = dna_transcribe.transcribe()
    # print(messenger_rna)
    # protein = messenger_rna.translate()
    # print(protein)

def dna(seq):
    """

    :return:
    """
    coding_dna = Seq(seq, IUPAC.unambiguous_dna)
    template_dna = coding_dna.reverse_complement()
    print("The corresponding mRNA to this sequence is:", template_dna)
    messenger_rna = Seq(template_dna, IUPAC.unambiguous_rna)
    protein = messenger_rna.translate()
    print("The corresponding protein to this sequence is:", protein)


def rna(seq):
    """

    :param seq:
    :return:
    """
    print("This is an RNA sequence:", seq)



def protein(seq):
    """

    :param seq:
    :return:
    """




main()
