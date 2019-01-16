# html_doc.py

# Lesson 139: Composition
# &
# Lesson 142: Aggregation

# When a class has a data object that is another
# class, that is 'composition'.

# From wikipedia: Aggregation differs from ordinary
# composition in that it does not imply ownership.
# In composition, when the owning object is destroyed,
# so are the contained objects.  In aggregation,
# this is not necessarily true.  For example, a
# university owns various departments (e.g., chemistry),
# and each department has a number of professors.
# If the university closes, the departments will no
# longer exist.  But, the professors in those
# departments will continue to exist.

# - Jim
# (contact info)


class Tag():
    
    def __init__(self, name, contents):
        self.start_tag = "<{0}>".format(name)
        self.end_tag = "</{0}>".format(name)
        
        self.contents = contents
    
    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
    
    def display(self, file=None):
        
        # Optionally was can save the contents out to a file.
        print(self, file=file)


class DocType(Tag):
    
    # Subclass of "Tag".
    
    def __init__(self):
        # Note: The "Doc Type" does not have any contents between the
        # open, and closing markers (<>, </>).  So, contents = ''.
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        
        # "end_tag" is defined in the call a/v.  However,
        # we need to overwrite its value b/c DOCTYPE do not
        # have an "end tag".
        self.end_tag = ''


class Head(Tag):
    
    # Subclass of "Tag".
    
    def __init__(self, input_title=None):
        # Starting out w/ an empty header.
        # But, it could have contents.
        super().__init__(name="head", contents="")
        
        # If a 'title' was passed in, then
        # create a 'title' tag inside the header
        # section:
        if input_title != None:

            # Input was suppled.  Create the title.
            self._title_tag = Tag('title', input_title)
            self.contents = str(self._title_tag)


class Body(Tag):
    
    # Subclass of "Tag".
    
    def __init__(self):
        # Starting out w/ an empty body.
        # To be built up w/ the "add_tag" method.
        super().__init__(name="body", contents="")

        self._body_contents = []
    
    def add_tag(self, name, contents):
        
        # Adds to the body's contents.
        new_tag = Tag(name=name, contents=contents)
        
        self._body_contents.append(new_tag)
    
    def display(self, file=None):
        
        # This is from the teacher.
        # I don't like it b/c, every time
        # you run it, you end up adding
        # existing tags to the "contents"
        # again.
        
        # Think the following line is needed:
        # (Create an empty slate):
        self.contents_to_display = str()
        
        # Build up the new body.
        for tag in self._body_contents:
            self.contents_to_display += str(tag)
        
        # Make it permanent:
        self.contents = self.contents_to_display
            
        super().display(file=file)
        

class HtmlDoc(object):
    
    def __init__(self, header_title=None):
        
        # An html page has the following
        # objects (and in that order).
        
        self._doc_type = DocType()
        self._head = Head(input_title=header_title)
        self._body = Body()
        
    def add_tag(self, name, contents):
        
        # For adding more content to the body
        # (what is displayed on the web page.
        self._body.add_tag(name=name, contents=contents)
        
    def display(self, file=None):
        
        self._doc_type.display(file=file)
        
        # We need to add in the beginning, and end "<html>" markers.
        print("<html>", file=file)
        
        self._head.display(file=file)
        self._body.display(file=file)
        
        # Closing the needed "<html>" tag.
        print("</html", file=file)


class HtmlDoc_Agg():
    
    # Same class as a/v but uses aggregation.
    
    def __init__(self, doc_type, head, body):
        
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        # For adding more content to the body
        # (what is displayed on the web page.
        self._body.add_tag(name=name, contents=contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
    
        # We need to add in the beginning, and end "<html>" markers.
        print("<html>", file=file)
    
        self._head.display(file=file)
        self._body.display(file=file)
    
        # Closing the needed "<html>" tag.
        print("</html", file=file)


#########################
# End Class Definitions #
#########################

# Are we running this python file, or
# importing it for its classes?
if __name__ == "__main__":
    
    # We are running it.
    
    # Composition example:

    my_page = HtmlDoc(header_title="Demo HMTL Document")
    my_page.add_tag("h1", "Main Heading")
    my_page.add_tag("h2", "sub-heading")
    my_page.add_tag("p", "This is a paragragh that will appear on the page.")
    
    test_doc_FH = open("test.html", "w")
    
    my_page.display(file=test_doc_FH)
    #my_page.display(file=test_doc_FH)
    
    test_doc_FH.close()
    
    ## Tested out some functions: (- Jim)
    # my_body = Body()
    # print(my_page is Tag)
    # print(isinstance(my_page, HtmlDoc))
    # print("isinstance(my_body, Body): ", isinstance(my_body, Body))
    # print("isinstance(my_body, Tag): ", isinstance(my_body, Tag))
    # print("issubclass(Body, Tag)", issubclass(Body, Tag))
    # print("issubclass(Body, Body)", issubclass(Body, Body))
    
    # Aggregation example:
    # (Elements are separate from the html doc object.
    
    new_docType = DocType()
    new_header = Head("Aggregation Example")
    
    new_body = Body()
    new_body.add_tag("h1", "Aggregation")
    new_body.add_tag("p", "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          " of objects to build up another object.")
    new_body.add_tag("p", "The aggregated object doesn't actually own the objects that were used to "
                          "create it.  If the object is destroyed, the objects w/i it, continue to exist!")
    
    
    # Create a new web page now that the previous one is
    # written to a file.
    my_page = HtmlDoc_Agg(new_docType, new_header, new_body)
    
    # Note "write" overwrites the whole doc.
    test_doc_2_FH = open("test2.html", "w")
    
    my_page.display(file=test_doc_2_FH)
    
    test_doc_2_FH.close()