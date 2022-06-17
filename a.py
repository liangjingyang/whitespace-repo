import logging
from typing import Iterable

from analysis.analysis_db import IndicatorFactory
from analysis.analyzer.aspect_graph_analyzer import CALL_ASPECT_GRAPH
from graphserver.call_aspect_graph_constants import CAG_DATA_LANGUAGE
from db.ca_report_models import RCagEdge

from analysis.report import check_existence, sources

_logger = logging.getLogger(__name__)


@check_existence(CALL_ASPECT_GRAPH)
@sources(CALL_ASPECT_GRAPH)
def gen_cag_edges(indicator_factory: IndicatorFactory, cag_indicator,
                  analysis_uuid: str) -> Iterable[RCagEdge]:
    for _, cag in cag_indicator.graphs.items():
        r_cag_edge: RCagEdge = RCagEdge()
        r_cag_edge.analysis_id = analysis_uuid
        r_cag_edge.language = data[CAG_DATA_LANGUAGE]
        yield r_cag_edge

