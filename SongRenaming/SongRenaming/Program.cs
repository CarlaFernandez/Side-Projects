using System;
using System.IO;
using System.Linq;
using System.Text;

namespace SongRenaming {
    class Program {

        /// <summary>
        /// Converts all song files from the given path to the standard:
        /// numTrack - songTitle
        /// </summary>
        /// <param name="args">File path, subfolder renaming</param>
        static void Main(string[] args) {
            string[] extensions = new string[] { ".mp3",".flac", ".rec",
            ".m4a",".aac",".wav",".mp4a", ".wma", ".ogg",};
            string path;
            if (args.Count() >= 1)
                path = @args[0];
            else {
                Console.WriteLine("You must write the path of your files");
                return;
            }
            bool renameSubfolders;
            if (args.Count() == 2)
                Boolean.TryParse(args[1], out renameSubfolders);
            else renameSubfolders = false;

            var filesInCurrentDir = Directory.GetFiles(path)
                .Where(file => extensions.Contains(Path.GetExtension(file))).ToList();
            var filesInSubDirs = Directory.GetDirectories(path)
                .SelectMany(dir => Directory.GetFiles(dir)
                .Where(file => extensions.Contains(Path.GetExtension(file)))).ToList();

            filesInCurrentDir.ForEach(filepath => Rename(filepath));
            if (renameSubfolders)
                filesInSubDirs.ForEach(filepath => Rename(filepath));

        }

        /// <summary>
        /// Applies the renaming algorithm to the current file
        /// </summary>
        /// <param name="filepath"></param>
        private static void Rename(string filepath) {
            TagLib.File file = TagLib.File.Create(@filepath);
            StringBuilder sb = new StringBuilder();
            sb.Append(file.Tag.Track).Append(" - ");
            sb.Append(file.Tag.Title);
            var pathWithoutFileName = Path.GetDirectoryName(filepath);
            var newFilePath = Path.Combine(pathWithoutFileName, sb.Append(Path.GetExtension(filepath)).ToString());
            Console.WriteLine("Renaming file {0} to {1}", Path.GetFileName(filepath), Path.GetFileName(newFilePath));
            File.Move(filepath, newFilePath);

        }
    }
}
