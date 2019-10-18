from PyPDF2 import PdfFileReader, PdfFileWriter

def doit (input,output):
    pdf_reader = PdfFileReader(input)
    pdf_writer = PdfFileWriter()

    n=pdf_reader.getNumPages();
    n = int (((n-1)/4)+1)*4;
    
    
    pdf_writer.appendPagesFromReader(pdf_reader)
    for i in range (0,(n-pdf_reader.getNumPages())):    
        pdf_writer.addBlankPage()
        print ("hadi");
    
    with open(output, 'wb') as out:
        pdf_writer.write(out)
    
    pdf_reader = PdfFileReader(output)
    pdf_writer = PdfFileWriter()
    K=(n+1);
    a=K;
    for i in range (1,n+1):
        if (i%4)==1:
            b=a-1;
            pdf_writer.addPage(pdf_reader.getPage(b-1))
            
        if (i%4)==2:
            c=K-b;
            pdf_writer.addPage(pdf_reader.getPage(c-1))
            
        if (i%4)==3:
            d=c+1;
            pdf_writer.addPage(pdf_reader.getPage(d-1))
            
        if (i%4)==0:
            a=K-d;
            pdf_writer.addPage(pdf_reader.getPage(a-1))


    with open(output, 'wb') as out:
        pdf_writer.write(out)


from PyPDF2 import PdfFileMerger

if __name__ == '__main__':
    doit ('Jazz.pdf','out.pdf');

'''
    merger = PdfFileMerger()
    merger.append('exam2.pdf',5)
    merger.write("result.pdf")
    merger.close()
'''
