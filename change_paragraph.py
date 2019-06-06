import docx

class Word(object):

    def input_data(paragraph,data,value):

        position=paragraph.text.find(data)+len(data)
        length=len(value)
        new = []
        for s in value:
            new.append(s)
        position_at=position
        for letter in new:        
            inline =paragraph.runs
            begin=0
            for i in range(len(inline)):
                if begin<=position_at<begin+len(inline[i].text) :
                    offset=position_at-begin
                    new = []
                    for s in inline[i].text:
                        new.append(s)
                    new[offset]=letter
                    inline[i].text=''.join(new)
                    position_at=position_at+1;
                    break 
                begin=begin+len(inline[i].text)
        return paragraph



if __name__ == "__main__":

    doc = docx.Document('Field Problem Feedback-Template.docx')

    for i in range(len(doc.paragraphs[0].runs)):
        print(doc.paragraphs[0].runs[0].text)
        print("size=",len(doc.paragraphs[0].runs[i].text))

    word=Word

    data="Entry Date："
    value="test"

    doc.paragraphs[0]=word.input_data(doc.paragraphs[0],data,value)
    doc.save('tmp.docx')

    for i in range(len(doc.paragraphs[0].runs)):
        print(doc.paragraphs[0].runs[0].text)
        print("size=",len(doc.paragraphs[0].runs[i].text))


























