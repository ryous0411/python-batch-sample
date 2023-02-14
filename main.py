import sys

from batch import Batch
from processor.game_result_processor import GameResultProcessor
from reader.game_result_reader import GameResultReader
from writer.game_result_writer import GameResultWriter

if __name__ == '__main__':
    game_winner_judgement_batch: Batch = \
        Batch(GameResultReader(), GameResultProcessor(), GameResultWriter())

    game_winner_judgement_batch.execute(sys.argv)
