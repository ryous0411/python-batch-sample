import sys

from src.batch import Batch
from src.processor.game_result_processor import GameResultProcessor
from src.reader.game_result_reader import GameResultReader
from src.writer.game_result_writer import GameResultWriter

if __name__ == '__main__':
    game_winner_judgement_batch: Batch = \
        Batch(GameResultReader(), GameResultProcessor(), GameResultWriter())

    game_winner_judgement_batch.execute(sys.argv)
