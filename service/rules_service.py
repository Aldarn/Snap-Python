from core.rules.suit_only_rules import SuitOnlyRules
from core.rules.value_only_rules import ValueOnlyRules
from core.rules.value_and_suit_rules import ValueAndSuitRules

RULES = {
	"suit": SuitOnlyRules(),
	"value": ValueOnlyRules(),
	"both": ValueAndSuitRules()
}

def getRulesFromInput(ruleType):
	return RULES.get(ruleType, None)
