import pytest
from deepeval import assert_test
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

from lib.model import get_custom_model


def test_case():
    model = get_custom_model()

    answer_relevancy_metric = AnswerRelevancyMetric(model=model, threshold=0.5)

    test_case = LLMTestCase(
        input = "鞋子如果不合脚怎么办？",
        actual_output = "我们提供30天全额退款，无需额外费用。",
        retrieval_context = ["所有客户均可享受30天无理由全额退款。"]
    )

    assert_test(test_case, [answer_relevancy_metric])