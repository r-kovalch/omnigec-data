from langchain_core.prompts import PromptTemplate

from src.prompts.reddit_multigec.czech     import MultiGrammarErrorCorrectionGenerationPrompt as CzMultiGecPrompt
from src.prompts.reddit_multigec.english   import MultiGrammarErrorCorrectionGenerationPrompt as EnMultiGecPrompt
from src.prompts.reddit_multigec.estonian  import MultiGrammarErrorCorrectionGenerationPrompt as EsMultiGecPrompt
from src.prompts.reddit_multigec.german    import MultiGrammarErrorCorrectionGenerationPrompt as GeMultiGecPrompt
from src.prompts.reddit_multigec.greek     import MultiGrammarErrorCorrectionGenerationPrompt as GrMultiGecPrompt
from src.prompts.reddit_multigec.icelandic import MultiGrammarErrorCorrectionGenerationPrompt as IcMultiGecPrompt
from src.prompts.reddit_multigec.italian   import MultiGrammarErrorCorrectionGenerationPrompt as ItMultiGecPrompt
from src.prompts.reddit_multigec.latvian   import MultiGrammarErrorCorrectionGenerationPrompt as LaMultiGecPrompt
from src.prompts.reddit_multigec.slovene   import MultiGrammarErrorCorrectionGenerationPrompt as SlMultiGecPrompt
from src.prompts.reddit_multigec.swedish   import MultiGrammarErrorCorrectionGenerationPrompt as SwMultiGecPrompt
from src.prompts.reddit_multigec.ukrainian import MultiGrammarErrorCorrectionGenerationPrompt as UkMultiGecPrompt

from src.prompts.reddit_multigec.czech     import GrammarErrorCorrectionAggregationPrompt as CzGecAggregationPrompt
from src.prompts.reddit_multigec.english   import GrammarErrorCorrectionAggregationPrompt as EnGecAggregationPrompt
from src.prompts.reddit_multigec.estonian  import GrammarErrorCorrectionAggregationPrompt as EsGecAggregationPrompt
from src.prompts.reddit_multigec.german    import GrammarErrorCorrectionAggregationPrompt as GeGecAggregationPrompt
from src.prompts.reddit_multigec.greek     import GrammarErrorCorrectionAggregationPrompt as GrGecAggregationPrompt
from src.prompts.reddit_multigec.icelandic import GrammarErrorCorrectionAggregationPrompt as IcGecAggregationPrompt
from src.prompts.reddit_multigec.italian   import GrammarErrorCorrectionAggregationPrompt as ItGecAggregationPrompt
from src.prompts.reddit_multigec.latvian   import GrammarErrorCorrectionAggregationPrompt as LaGecAggregationPrompt
from src.prompts.reddit_multigec.slovene   import GrammarErrorCorrectionAggregationPrompt as SlGecAggregationPrompt
from src.prompts.reddit_multigec.swedish   import GrammarErrorCorrectionAggregationPrompt as SwGecAggregationPrompt
from src.prompts.reddit_multigec.ukrainian import GrammarErrorCorrectionAggregationPrompt as UkGecAggregationPrompt


multi_gec_prompt_per_language: dict[str, PromptTemplate] = {
    "czech":     CzMultiGecPrompt(),
    "english":   EnMultiGecPrompt(),
    "estonian":  EsMultiGecPrompt(),
    "german":    GeMultiGecPrompt(),
    "greek":     GrMultiGecPrompt(),
    "icelandic": IcMultiGecPrompt(),
    "italian":   ItMultiGecPrompt(),
    "latvian":   LaMultiGecPrompt(),
    "slovene":   SlMultiGecPrompt(),
    "swedish":   SwMultiGecPrompt(),
    "ukrainian": UkMultiGecPrompt(),
}
gec_aggregation_prompt_per_language: dict[str, PromptTemplate] = {
    "czech":     CzGecAggregationPrompt(),
    "english":   EnGecAggregationPrompt(),
    "estonian":  EsGecAggregationPrompt(),
    "german":    GeGecAggregationPrompt(),
    "greek":     GrGecAggregationPrompt(),
    "icelandic": IcGecAggregationPrompt(),
    "italian":   ItGecAggregationPrompt(),
    "latvian":   LaGecAggregationPrompt(),
    "slovene":   SlGecAggregationPrompt(),
    "swedish":   SwGecAggregationPrompt(),
    "ukrainian": UkGecAggregationPrompt(),
}
