import streamlit as st
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
codontab = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}
def gcContent(seq):
    total=0
    for c in seq:
        if c == 'G'or c == 'C':
            total+=1

    percentage=total/len(seq)
    return f"%{percentage*100:.2f}"

def complement(seq):
    complement_dict = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"
    }
    return "".join([complement_dict[x] for x in seq])

def rna(seq):
    return seq.upper().replace("T", "U")
def aminoacid(seq):
    a_acid=[]
    if len(seq)%3!=0:
        warning=f"Warning: Length not divisible by 3. Last {len(seq) % 3} bases ignored."
    else:
        warning=""
    for i in range(0, len(seq) - len(seq) % 3, 3):
        codon = seq[i:i + 3]
        if codon in codontab:
            a_acid.append(codontab[codon])

    return warning + "".join(a_acid)

def alignment(seq1,seq2):
    seq1=seq1.upper()
    seq2=seq2.upper()
    alignments=pairwise2.align.globalxx(seq1,seq2)
    if alignments:
        best_alignment=alignments[0]
        return format_alignment(*best_alignment)
    else:
        return ""

functions={
    "gcContent":"gcContent",
    "complement":"complement",
    "rna":"rna",
    "aminoacid":"aminoacid",
    "align":"alignment"

}


st.title("Bioinformatics")
result=st.selectbox("Select a function",list(functions.keys()))
st.divider()
st.subheader(f"Function:{result}")
if functions[result]=="gcContent":
    seq=st.text_input("Enter a sequence")
    if st.button("Calculate GC Content"):
        st.info(f"Result: {gcContent(str(seq))}")
elif functions[result]=="complement":
    seq=st.text_input("Enter a sequence")
    if st.button("Calculate Complement"):
        st.info(f"Result: {complement(str(seq))}")
elif functions[result]=="rna":
    seq=st.text_input("Enter a sequence")
    if st.button("Calculate RNA Content"):
        st.info(f"Result: {rna(str(seq))}")

elif functions[result]=="aminoacid":
    seq=st.text_input("Enter a sequence")
    if st.button("Calculate Aminoacid"):
        st.info(f"Result: {aminoacid(str(seq))}")

elif functions[result]=="alignment":
    seq1=st.text_input("Enter a sequence")
    seq2=st.text_input("Enter another sequence")
    if st.button("Calculate Alignment"):
        st.code(f"Result: {alignment(str(seq1),str(seq2))}",language="text")
