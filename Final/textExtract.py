import PyPDF2
import textract
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
import docx
# %matplotlib inline


def pdfFileScan(file, name, ):
    # Open pdf file

    # Initialize a text empty etring variable
    text = ""
    try:
        pdfFileObj = open(file, 'rb')

        # Read file
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # Get total number of pages
        num_pages = pdfReader.numPages

        # Initialize a count for the number of pages
        count = 0

        # Extract text from every page on the file
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count += 1
            text += pageObj.extractText()

        # Convert all strings to lowercase
        text = text.lower()

        # Remove numbers
        text = re.sub(r'\d+', '', text)

    except:
        doc = docx.Document(file)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            text = '\n'.join(fullText)
            # Convert all strings to lowercase
            text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Create dictionary with industrial and system engineering key terms by area
    terms = {'MultiTasking': ['organization', 'prioritization', 'deadlines', 'managing expectations', 'planning', 'strategic planning',
                              'stress tolerance'],
             'Attention to details': ['analytical skills', 'troubleshooting', 'technical tocumentation','tormulas',
                                      'data analytics', 'creativity', 'critical thinking', 'problem solving', 'deductive reasoning',
                                      'inductive reasoning', 'process analysis' ],
             'Supply chain': ['abc analysis', 'apics', 'customer', 'customs', 'delivery', 'distribution', 'eoq', 'epq',
                              'fleet', 'forecast', 'inventory', 'logistic', 'materials', 'outsourcing', 'procurement',
                              'reorder point', 'rout', 'safety stock', 'scheduling', 'shipping', 'stock', 'suppliers',
                              'third party logistics', 'transport', 'transportation', 'traffic', 'supply chain',
                              'vendor', 'warehouse', 'wip', 'work in progress'],
             'Project management': ['administration', 'agile', 'budget', 'cost', 'direction', 'feasibility analysis',
                                    'finance', 'kanban', 'leader', 'leadership', 'management', 'milestones', 'planning',
                                    'pmi', 'pmp', 'problem', 'project', 'risk', 'schedule', 'scrum', 'stakeholders'],
             'Data analytics': ['analytics', 'api', 'aws', 'big data', 'busines intelligence', 'clustering', 'code',
                                'coding', 'data', 'database', 'data mining', 'data science', 'deep learning', 'hadoop',
                                'hypothesis test', 'iot', 'internet', 'machine learning', 'modeling', 'nosql', 'nlp',
                                'predictive', 'programming', 'python', 'r', 'sql', 'tableau', 'text mining',
                                'visualization'],
             'Software Development':['javascript', 'sql', 'sequel','java', 'ruby', 'php', 'python','c++', 'C#','html','xml',
                                     'css', 'react.js', 'angular.js', 'django',  'starlette', 'gunicorn', 'laravel', 'database architecture',
                                     'database', 'algorithms', 'data structures', 'product enhancement', 'linux', 'unix',
                                     'perl','shell', 'optimization', 'design reviews', 'design', 'agile scrum team', 'computer architecture',
                                     'operating systems', 'saas', 'web services', 'source code', 'version Repository', 'ui toolkits', 'frameworks',
                                     'microsoft ASP.NET', 'web api', 'node.js', 'deno.js']}

    # Initializie score counters for each area
    quality = 0
    operations = 0
    supplychain = 0
    project = 0
    data = 0
    healthcare = 0

    # Create an empty list where the scores will be stored
    scores = []

    # Obtain the scores for each area
    for area in terms.keys():

        if area == 'Quality/Six Sigma':
            for word in terms[area]:
                if word in text:
                    quality += 1
            scores.append(quality)

        elif area == 'Operations management':
            for word in terms[area]:
                if word in text:
                    operations += 1
            scores.append(operations)

        elif area == 'Supply chain':
            for word in terms[area]:
                if word in text:
                    supplychain += 1
            scores.append(supplychain)

        elif area == 'Project management':
            for word in terms[area]:
                if word in text:
                    project += 1
            scores.append(project)

        elif area == 'Data analytics':
            for word in terms[area]:
                if word in text:
                    data += 1
            scores.append(data)

        else:
            for word in terms[area]:
                if word in text:
                    healthcare += 1
            scores.append(healthcare)

    # Create a data frame with the scores summary
    summary = pd.DataFrame(scores, index=terms.keys(), columns=['score']).sort_values(by='score', ascending=False)
    skills= summary.to_dict()
    # print(skills)

    # # Create pie chart visualization
    # pie = plt.figure(figsize=(10, 10))
    # plt.pie(summary['score'], labels=summary.index, explode=(0.1, 0, 0, 0, 0, 0), autopct='%1.0f%%', shadow=True,
    #         startangle=90)
    # plt.title('Software Engineering Candidate - Resume Decomposition by Areas')
    # plt.axis('equal')
    #
    # # Save pie chart as a .png file
    # image = pie.savefig('{}_screening_results.png'.format(name))

    return skills