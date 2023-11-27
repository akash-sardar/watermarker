import PyPDF2
import os
import sys

def pdfcombiner(files):
    merger = PyPDF2.PdfFileMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write(os.path.join(infp,'merged.pdf'))

def watermarker(file, wtrfile):
    infile = PyPDF2.PdfFileReader(open(file,'rb'))
    wtr = PyPDF2.PdfFileReader(open(wtrfile,'rb'))
    output = PyPDF2.PdfFileWriter()
    for i in range(infile.numPages):
        page = infile.getPage(i)
        page.mergePage(wtr.getPage(0))
        output.addPage(page)
    with open(os.path.join(infp,'watermarked_output.pdf'),'wb') as out:
        output.write(out)


if __name__ == '__main__':
    infp = 'C:\\Akash\\LearningDocuments\\Python\\Projects\\PDFProject\\input files\\'
    inputs = sys.argv[1:]
    files = list()
    for input in inputs:
        file = os.path.join(infp,input)
        if os.path.isfile(file) and file.split('.')[1] == 'pdf':
            files.append(file)
        else:
            continue
    pdfcombiner(files)
    infilepath = os.path.join(infp,'merged.pdf')
    watermark = os.path.join(infp,'wtr.pdf')
    watermarker(infilepath, watermark)



