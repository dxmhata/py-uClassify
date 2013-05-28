'''
Created on Dec 25, 2011

@author: debanjan
'''
import urllib2

class uClassify:
    '''Main Class for using the uClassify API'''
    
    __classifier = ""
    __api_key = ""
    __urlToClassify = ""
    __outputFormat = ""
    
    def classifyURL(self,choice = 'null'):
        '''Helps to choose the classifier from the following list which are
            also available at http://www.uclassify.com/browse:
            1.Sentiment : choice = 'sentiment'
            2.Text Language : choice = 'language'
            3.Topics : choice = 'topic'
            4.GenderAnalyzer: choice = 'gender'
            5.Mood: choice = 'mood'
            6.Age: analyzer = 'age'
            7.Myers Briggs Judging Function : choice = 'myersjudge'
            8.Society topics: choice = 'society'
            9.Tonality : choice = 'tone'
            10.News : choice = 'news'
            11.Myers Briggs Lifestyle : choice = 'myerslifestyle'
            12.Myers Briggs Attitude : choice = 'myersattitude'
            13.Home topics : choice = 'home'
            14.Art topics : choice = 'art'
            15.Game topics: choice = 'games'
            16.Health topics : choice = 'health'
            17.Computer topics : choice = 'computer'
            18.Business topics : choice = 'business'
            19.Recreation topics : choice = 'recreation'
            20.Sport topics : choice = 'sports'
            21.Science topics : choice = 'science'
            22.MySpamFilter : choice = 'spam'
            '''
        
        if choice == 'sentiment':
            response = self.__classifySentiment()
            return response
        
        elif choice == 'language':
            response = self.__classifyLanguage()
            return response
                    
        elif choice == 'topic':
            response = self.__classifyTopics()
            return response
        
        elif choice == 'gender':
            response = self.__classifyGender()
            return response
        
        elif choice == 'mood':
            response = self.__classifyMood()
            return response
        
        elif choice == 'age':
            response = self.__classifyAge()
            return response
        
        elif choice == 'myersjudge':
            response = self.__classifyMyersjudge()
            return response
        
        elif choice == 'society':
            response = self.__classifySocietyTopics()
            return response
        
        elif choice == 'tone':
            response = self.__classifyTone()
            return response
        
        elif choice == 'news':
            response = self.__classifyNewsTopics()
            return response
        
        elif choice == 'myerslifestyle':
            response = self.__classifyMyerslifestyle()
            return response
        
        elif choice == 'myersattitude':
            response = self.__classifyMyersattitude()
            return response
        

        elif choice == 'home':
            response = self.__classifyHomeTopics()
            return response
        
        elif choice == 'art':
            response = self.__classifyArtTopics()
            return response
        
        elif choice == 'games':
            response = self.__classifyGamesTopics()
            return response
        
        elif choice == 'health':
            response = self.__classifyHealthTopics()
            return response
        
        elif choice == 'computer':
            response = self.__classifyComputerTopics()
            return response
        
        elif choice == 'business':
            response = self.__classifyBusinessTopics()
            return response
        
        elif choice == 'recreation':
            response = self.__classifyRecreationTopics()
            return response
        
        elif choice == 'sports':
            response = self.__classifySportsTopics()
            return response
        
        elif choice == 'science':
            response = self.__classifyScienceTopics()
            return response
        
        elif choice == 'spam':
            response = self.__classifySpam()
            return response
        else:
            return "Please enter a valid choice"
            



    def __classifySentiment(self):
        '''This classifier determines if a text is positive or negative. It can
         be used to conduct market research, brand surveys and see trends around
         campaigns. It's based on about 40000 Amazon product
         reviews (collected by Mark Dredze cs.jhu.edu/~mdredze/datasets/sentiment/) 
         and mood training data (by mattiasostmar.net)'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Sentiment/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
        

    def __classifyLanguage(self):
        '''Classifies using sentiment classifier: http://www.uclassify.com/browse/uClassify/Sentiment
            Returns the overall sentiment of the document of the url as positive or negative'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Text%20Language/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyTopics(self):
        '''Categories an English text into a topic (Arts, Business, Computers, 
        Games, Health, Home, Recreation, Science, Society and Sports). Each of 
        those topics has more specific child classifier (Art Topics, Business 
        Topics etc). It uses a subset of topics from the Open Directory Project 
        at http://www.dmoz.org.'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyGender(self):
        '''This classifier tries to figure out if a text is written by a male or female.
         It has been trained on 11000 blogs (5500 blogs wrtten by females and 5500 by males). 
         More text gives better results.'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/GenderAnalyzer_v5/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyMood(self):
        '''The state of mind of the writer - upset or happy. On the extreme side
         there is angry, hateful writers and on the other extreme there is joyful
         and loving writers. The measured accuracy is 96% (using 10-fold cross validation).
         For reliable results we recommend that you use at least 200 words. 
         Currently works for English texts.'''
        
        baseUrl = "http://uclassify.com/browse/prfekt/Mood/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyAge(self):
        '''This classifier tries to estimate to which age group a blog belongs. 
        The training data is based upon about 7000 blogs collected randomly from Internet.'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Ageanalyzer/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyMyersjudge(self):
        '''Determines the Thinking/Feeling dimension of the personality type according 
        to Myers-Briggs personality model. The analysis is based on the writing style and
        should NOT be confused with the MBTI (c) which determines personality type based 
        on self-assessment questionnaires. Currently works for English texts. 
        Swedish version available on request. '''
        
        baseUrl = "http://uclassify.com/browse/prfekt/Myers%20Briggs%20Judging%20Function/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifySocietyTopics(self):
        '''Categories an English text into a society topic. Use the parent classifier 'Topics' 
        to find out if a text belongs in this category. It uses a subset of topics from the 
        Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Society%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyTone(self):
        '''Determines the tonality of a text - corporate (formal) or personal (informal). 
        Helps distinguish between prosumer media and pro media for instance. 
        Currently works for English texts.'''
        
        baseUrl = "http://uclassify.com/browse/prfekt/Tonality/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyNewsTopics(self):
        '''This classifier categorizes news articles. It was trained with 1000 hand picked articles from 
        major news sources per category. The text used was a combination of each article's title, 
        description and scraped and cleaned text.'''
        
        baseUrl = "http://uclassify.com/browse/mvazquez/News%20Classifier/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyMyerslifestyle(self):
        '''Determines the Judging/Perceiving dimension of the personality type according
         to Myers-Briggs personality model. 
         The analysis is based on the writing style and should NOT be confused with the MBTI (c) 
         which determines personality type based on self-assessment questionnaires. 
         Currently works for English texts. Swedish version available on request.'''
        
        baseUrl = "http://uclassify.com/browse/prfekt/Myers%20Briggs%20Lifestyle/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyMyersattitude(self):
        '''Analyzes the Extraversion/Introversion dimension of the personality type according
         to Myers-Briggs personality model. The analysis is based on the writing style 
         and should NOT be confused with the MBTI (c) which determines personality type 
         based on self-assessment questionnaires. Currently works for English texts. 
         Swedish version available on request.'''
        
        baseUrl = "http://uclassify.com/browse/prfekt/Myers%20Briggs%20Attitude/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    
    def __classifyHomeTopics(self):
        '''Categories an English text into a home topic. Use the parent classifier 'Topics' 
        to find out if a text belongs in this category. It uses a subset of topics from the 
        Open Directory Project at http://www.dmoz.org.'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Home%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyArtTopics(self):
        '''Categories an English text into an art topic. Use the parent classifier 'Topics' to 
        find out if a text belongs in this category. It uses a subset of topics from 
        the Open Directory Project at http://www.dmoz.org.'''

        baseUrl = "http://uclassify.com/browse/uClassify/Art%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()        
    
    def __classifyGamesTopics(self):
        '''Categories an English text into a game topic. 
        Use the parent classifier 'Topics' to find out if a text belongs in this category. 
        It uses a subset of topics from the Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Game%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyHealthTopics(self):
        '''Categories an English text into a health topic. 
        Use the parent classifier 'Topics' to find out if a text belongs in this category. 
        It uses a subset of topics from the Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Health%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyComputerTopics(self):
        '''Categories an English text into a computer topic. 
        Use the parent classifier 'Topics' to find out if a text belongs in this category. 
        It uses a subset of topics from the Open Directory Project at http://www.dmoz.org.'''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Computer%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyBusinessTopics(self):
        '''Categories an English text into an business topic. 
        Use the parent classifier 'Topics' to find out if a text belongs in this category. 
        It uses a subset of topics from the Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Business%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyRecreationTopics(self):
        '''Categories an English text into a recreation topic. 
        Use the parent classifier 'Topics' to find out if a text belongs in this category. 
        It uses a subset of topics from the Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Recreation%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifySportsTopics(self):
        '''Categories an English text into a sport topic.
         Use the parent classifier 'Topics' to find out if a text belongs in this category. 
         It uses a subset of topics from the Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Sport%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifySpam(self):
        '''Classifies the document of the given URL as a legitimate or an illegitimate one'''
        
        baseUrl = "http://uclassify.com/browse/khodrog/MySpamFilter/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()
    
    def __classifyScienceTopics(self):
        '''Categories an English text into a science topic.
         Use the parent classifier 'Topics' to find out if a text belongs in this category. 
         It uses a subset of topics from the Open Directory Project at http://www.dmoz.org. '''
        
        baseUrl = "http://uclassify.com/browse/uClassify/Science%20Topics/ClassifyUrl?"
        requestUrl = baseUrl+"readkey="+uClassify.__api_key+"&url="+uClassify.__urlToClassify+"&version=1.01"+"&output="+uClassify.__outputFormat
        response = urllib2.urlopen(requestUrl)
        return response.read()  
    
    
    def setApiKey(self,key="null"):
        '''Helps in setting the read API key obtained from uClassify'''
        if key == "null":
            print("Please enter a valid key")
        else:
            uClassify.__api_key = key
    
    def setUrlToClassify(self,url="null"):
        '''Helps in setting url of the document for classification'''
        if url == 'null':
            print("Please enter a valid url to classify")
        else:
            uClassify.__urlToClassify = url
            
    def setOutputFormat(self,format = "null"):
        '''Helps in setting the output format of the result as xml or json'''
        if format == 'json':
            uClassify.__outputFormat = "json"
        elif format == 'xml':
            uClassify.__outputFormat = "xml"
        else:
            print ("The only allowed output formats are 'xml' and 'json', Please enter a valid format in setOutputFormat() ")
        
            
             
    
        
        