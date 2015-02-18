import core.rules.suit_only_rules.SuitOnlyRules as SuitOnlyRules
import core.rules.value_only_rules.ValueOnlyRules as ValueOnlyRules
import core.rules.value_and_suit_rules.ValueAndSuitRules as ValueAndSuitRules

RULES = {
	"suit": lambda: SuitOnlyRules(),
	"value": lambda: ValueOnlyRules(),
	"both": lambda: ValueAndSuitRules()
}

def getRulesFromInput(ruleType):
	return RULES.get(ruleType, None)
