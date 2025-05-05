from src.prompts.base_prompts import BasePrompt


class MultiGrammarErrorCorrectionGenerationPrompt(BasePrompt):
    template: str = """Correct the following text by making it grammatically correct.
Correct all spelling, punctuation, stylistic, grammatical, lexical, and syntactic errors.
If there are no errors, simply repeat the original text.
Generate {num_corrections} distinct versions of the corrected text along with explanations.
Escape all double quotes and other special characters in your answer using two backslashes.
For example, instead of a newline use \\n; instead of " use \\".
Please do not remove technical symbols such as internet links, tags, etc. from other languages (primarily English).


Response format in JSON:
[{{
    "correction": "corrected text",
    "explanation": "explanation for the correction"
}}, ...]

Examples:

1. Input text:
   There are lots of important things in our life. However, in most cases, they depend on the priorities we have and acceptation we are awaiting from it. If it fulfils our dreams and aims or not? First of all, let us start with one of the most important things in our life and that is health. Our mind and body will be so much satisfied as we give our body at least the minimum of our time. What I am trying to say is that a certain form of physical activity per week is beneficial in many facets of our life. That is to say, If you lead an active life, your body appreciate it when you get older. On the other hand, those who prefer not to have an active life and their efforts to put their time in any kind of activity have a bad perspective when they get older. Moreover, their lifestyle is probably aimed to work and earning money. All things considered, it seems reasonable to revise our free time and to think it over, if we have what we wanted.

   Corrections:
   [("There are lots of important things in our life. However, in most cases, they depend on the priorities we have and the expectations we hold. First of all, let us begin with one of the most vital aspects—our health. Our mind and body will be very satisfied if we devote at least a minimal amount of time to them. In essence, engaging in regular physical activity benefits many aspects of our life. That is to say, if you lead an active life, your body will appreciate it as you age. Conversely, those who choose a sedentary lifestyle and fail to dedicate time to any form of activity tend to face negative consequences later in life. Moreover, their lifestyle is probably focused on work and earning money. All things considered, it seems reasonable to re-evaluate our free time and ask ourselves whether we have achieved what we truly desired.", "Revised awkward phrases, standardized word choices, and corrected punctuation for clarity."), 
   ("There are many important aspects of our lives, yet in most cases they depend on the priorities we set and the expectations we have. To begin, consider our health—the foundation of everything. Our mind and body benefit greatly when we allocate even a small portion of our time to self-care. Essentially, regular physical activity can improve many facets of our life. On the other hand, a lack of activity may lead to negative outcomes as we grow older, especially when life is overly centered on work and money. Therefore, it is wise to reconsider how we spend our free time.", "Rephrased for better flow, corrected grammatical inconsistencies, and adjusted punctuation."), 
   ("Our lives are filled with important elements, but they often hinge on the priorities we choose and the expectations we nurture. Consider health, for example: devoting even a minimal amount of time to physical activity can yield tremendous benefits for both body and mind. In contrast, neglecting such activity might result in adverse effects as one ages—especially in a lifestyle driven by work and the pursuit of money. Ultimately, it makes sense to re-assess our free time to ensure we are truly living as we wish.", "Condensed and restructured the original text to improve readability and coherence.")]

2. Input text:
   When we are talking about travel, we have to reduce our thinking only about the available method of transportation. There are a variety of transport systems available at the moment. For instance, we can travel on the railway, on the road, in the air and the last possible choice is under the ground. That sounds good. We can travel anywhere and anytime we want. However, if we are want to be somewhere at a specific time and something has happened on our journey, what would we do? Well, the solution is in science and the future. As I have read in the last six months, most of the companies have been trying to bring a solution to get somewhere faster than now. Any researchers brought fast trains and other fast cars. what is more, there is also a car that provides its passengers to get to the airport faster than by taxi. That is a car use a similar system as planes do, but for short distances. Maybe it is a future for the transport system in big towns. It does not produce any emissions lake carbon or sound. As far as I am concerned, I guess that the future of transportation, let say travelling in the air is an issue number one. Finally, it seems reasonable to act for supporting science. There is no choice for the future if we do not want to destroy our environment completely.

   Corrections:
   [("When discussing travel, we should limit our focus to the available methods of transportation. There are various transport systems available today. For instance, we can travel by railway, by road, by air, or even underground. That sounds promising since it means we can travel anywhere at any time. However, if we want to reach a destination at a specific time and something goes wrong during our journey, what would we do? The solution lies in scientific innovation and future technology. Over the past six months, many companies have been working to develop faster ways to travel—introducing high-speed trains and automobiles. Furthermore, there is a car that allows passengers to reach the airport quicker than a taxi by using a system similar to that of airplanes, but designed for short distances. Perhaps this represents the future of transportation in major cities. It produces no emissions like carbon dioxide and operates quietly. In my view, the future of transportation—especially air travel—is a top priority. Finally, it seems reasonable to support science, as our future depends on it.", "Corrected prepositions, refined sentence structures, and standardized terminology."), 
   ("When talking about travel, our consideration should be limited to the available modes of transportation. Today, transport systems include railways, roads, air travel, and even underground options. This diversity means we can reach any destination at any time. But if an unexpected issue occurs when we need to be somewhere at a specific time, what can we do? The answer lies in science and future advancements. In recent months, many companies have introduced faster travel solutions, such as high-speed trains and cars. Notably, a new car model enables passengers to get to the airport faster than a taxi by using technology similar to that of airplanes for short distances. This may well signal the future of urban transportation—offering reduced emissions and minimal noise. In summary, advancing scientific innovation is crucial for our future.", "Improved clarity, corrected grammar, and restructured sentences for better flow."), 
   ("Our discussion on travel should focus solely on the available transportation methods. Currently, these include railways, roads, air travel, and underground routes. Such options allow for travel at any time and to almost any destination. However, if you need to be somewhere punctually and an issue arises during the journey, what is the remedy? Science and future technology offer the solution. In the past six months, several companies have been developing rapid travel solutions, including fast trains and automobiles. Additionally, a car has been introduced that gets passengers to the airport more quickly than traditional taxis by using a system akin to that of airplanes—albeit for short distances. This innovation could very well represent the future of transportation in large urban areas, with benefits like zero harmful emissions and low noise levels. I believe that supporting such scientific progress is essential.", "Rephrased to enhance precision, fixed syntactical errors, and adjusted punctuation appropriately.")]

3. Input text:
   In which way the travel will change ? Firstly, by energy. In fact, electric cars are at their apogee, so they can evolue in future energy that is more ecological, less and available. This is actually due to ecological factors and because of the breach of resources. Secondly, because of the design of the cars, there is more technological aspect to cars and it might represent cars of the future. These cars are in new design never seen before like round car, faster, bigger, smaller etc... But the aspect of a car influe notably on his form, this is the aerodynamic that ameliore cars and let them be more beautiful and faster. To conclude, the design is assiocated with the speed factor of cars, and the energy is evoluing so the future car is probably with an inconnue energy, and with a really awesome design that would be surprised everyone. Goodbye see you again !

   Corrections:
   [("In what way will travel change? Firstly, in terms of energy. In fact, electric cars are at their peak and may evolve to use future energy sources that are more ecological, efficient, and accessible. This shift is driven by environmental factors and diminishing resources. Secondly, advances in car design are introducing more technological features, which may define the cars of the future. These vehicles showcase innovative designs never seen before—such as rounded shapes, varied sizes, and enhanced speed. Moreover, a car’s design significantly influences its aerodynamics, making it both more attractive and faster. In conclusion, as energy evolves, future cars may rely on unconventional energy sources and feature striking designs that astonish everyone. Goodbye, and see you again!", "Corrected word order, improved vocabulary choices, and adjusted punctuation for clarity."), 
   ("How will travel change? First, regarding energy. Electric cars, now at their zenith, might evolve to harness energy that is more sustainable, efficient, and readily available. This change is largely due to environmental concerns and resource limitations. Second, innovative car designs are adding advanced technological aspects that could define the vehicles of tomorrow. These futuristic cars, with entirely new design concepts—featuring rounded exteriors, varying dimensions, and superior speed—demonstrate how improved aerodynamics can enhance both form and function. Ultimately, design and energy innovations are closely intertwined, suggesting that future cars may operate on novel energy sources and boast remarkable aesthetics. Farewell until next time!", "Streamlined sentence structure, corrected grammatical inconsistencies, and enriched the vocabulary."), 
   ("What changes can we expect in travel? To begin with, energy will play a crucial role. Electric cars, which are currently at their peak performance, might evolve to utilize energy that is more ecological, efficient, and widely available. This evolution is driven by environmental factors and the depletion of traditional resources. Additionally, cutting-edge car designs are incorporating more technological features, potentially shaping the vehicles of the future. These innovative designs—ranging from rounded shapes to varied sizes and speeds—highlight the importance of aerodynamics in enhancing both appearance and performance. In summary, as energy sources evolve, future cars may rely on unconventional power and exhibit designs that truly surprise. Goodbye and see you soon!", "Enhanced clarity and cohesiveness by reordering sentences, refining word choices, and ensuring proper punctuation.")]

Input text: {text}
Corrections:"""


class GrammarErrorCorrectionAggregationPrompt(BasePrompt):
    template: str = """Aggregate the proposed grammar corrections into a final, grammatically correct text.
From the original text and a list of {num_corrections} correction variants, merge all the useful changes from these versions to create one final, syntactically correct text.
Eliminate all spelling, punctuation, stylistic, grammatical, lexical, and syntactic errors.
Include explanations for the aggregated corrections and the overall grammar fixes.
Focus solely on the suggested corrections and do not attempt to independently modify the original text.
If there are no errors, return the original text.
Escape all double quotes and other special characters in your response using two backslashes.
For example, use \\n for a newline and \\" for a double quote.
Please do not remove technical symbols such as internet links, tags, etc. from other languages (primarily English).


Format for the proposed corrections:
[{{
    "correction": "corrected text",
    "explanation": "explanation for the correction"
}},...]

[Output only JSON]
Response format in JSON:
{{
    "correction": "corrected text",
    "explanation": "explanation for the correction"
}}

Original text: {text}
Proposed corrections: {possible_corrections}
Corrected text:"""
    input_variables: list[str] = ["text", "possible_corrections", "num_corrections"]

