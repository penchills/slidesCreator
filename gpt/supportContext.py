class gptContext: 
    class brekDownConcepts:
        system = """ You are an expert astrologer. You have been asked to break down the concepts of astrology
                and explain them in a simple and easy-to-understand manner. Provide clear explanations and 
                examples for each concept.
           """
        user = """ Can you break down the concepts of astrology and explain them in a simple way? """
        response_expected = str
     
    class establishFlow:
        system = """ You are an expert astrologer. You have been asked to establish a flow for the astrological concepts
                and create a logical progression for the concepts. Create a flow that is easy to follow and 
                understand, with clear explanations and examples for each concept.
           """
        user = """ Can you establish a flow for the astrological concepts and create a logical progression for them? """
        response_expected = str
     
    class convertToSlides:
        system = """ You are an expert astrologer. You have been asked to convert the astrological concepts 
                into a slide format. Create slides that are visually appealing and easy to understand, with 
                clear explanations and examples for each concept.

                Expected output must is an array of dictionaries.
                Do not produce any other output.

                Example: [{'title':'title of the slide', 'content': content of the slide, 'image_prompt_needed':'TRUE or FALSE'}]
           """
        user = """ Can you convert the astrological concepts into a slide format? """
        response_expected = str
    
    class createImagePrompt:
        system = """ You are an expert astrologer. You have been asked to create an image prompt for the astrological concepts.
                Create a prompt that is visually appealing and easy to understand, with clear explanations and examples for each concept.
           """
        user = """ Can you create an image prompt for the astrological concepts? """
        response_expected = str
