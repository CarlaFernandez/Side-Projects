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
        /// <param name="args">File path</param>
        static void Main(string[] args) {
            string[] extensions = new string[] { ".mp3",".flac", ".rec",
            ".m4a",".aac",".wav",".mp4a", ".wma", ".ogg",};
            var path = @args[0];
            bool renameSubfolders;
            bool areThereSubfolders;
            // TODO: exceptions
            Boolean.TryParse(args[1], out renameSubfolders);
            areThereSubfolders = Directory.GetDirectories(path).Count().Equals(0);
            Console.WriteLine(areThereSubfolders);
            // TODO: make it work with subfolders
            // if there are subfolders and subfolder renaming is checked, rename everything
            //var filepaths = areThereSubfolders && renameSubfolders ?
            //    Directory.GetDirectories(path).ToArray().SelectMany(dir => Directory.GetFiles(dir)).Where(file => {
            //        foreach (string extension in extensions) {
            //            if (Path.GetExtension(file).Equals(extension))
            //                return true;
            //        }
            //        return false;
            //    })
            //// otherwise, rename only the files in the path folder
            //:
            //Directory.GetFiles(path).Where(file => {
            //    foreach (string extension in extensions) {
            //        if (file.ToString().Contains(extension))
            //            return true;
            //    }
            //    return false;
            //});

            //foreach (var filepath in filepaths) {
            //    TagLib.File file = TagLib.File.Create(@filepath);
            //    StringBuilder sb = new StringBuilder();
            //    sb.Append(file.Tag.Track).Append(" - ");
            //    sb.Append(file.Tag.Title);
            //    var pathWithoutFileName = Path.GetDirectoryName(filepath);
            //    var newFilePath = Path.Combine(pathWithoutFileName, sb.ToString() + Path.GetExtension(filepath));
            //    Console.WriteLine("Renaming file {0} to {1}", filepath, newFilePath);
            //    File.Move(filepath, newFilePath);

            //}

        }
    }
}
